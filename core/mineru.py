# -*- coding: utf-8 -*-
"""
统一 MinerU 文档解析驱动器
支持云端 OpenAPI (v4) 自动上传解析与本地目录数据装配，兼容论文与大型专著。
"""

import os
import sys
import glob
import json
import time
import zipfile
import requests
from typing import Tuple, Dict, Optional, Callable

from core.config import MINERU_TOKEN
from core.sentinel import formula_fingerprint

MINERU_API_BASE = "https://mineru.net/api/v4"

class MinerUClient:
    def __init__(self, token: Optional[str] = None):
        self.token = token or MINERU_TOKEN
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def extract_pdf(self, pdf_path: str, output_dir: str, log_cb: Optional[Callable[[str], None]] = None) -> str:
        """
        调用 MinerU 提取 PDF 内容并解压到 output_dir。
        若 output_dir 下已存在解析好的 content_list.json，则自动跳过上传直接复用。
        """
        os.makedirs(output_dir, exist_ok=True)
        pdf_name = os.path.basename(pdf_path)

        def log(msg):
            if log_cb:
                log_cb(msg)
            else:
                print(f"[MinerU] {msg}")

        # 检查是否已存在解析产物
        existing_lists = glob.glob(os.path.join(output_dir, "*content_list*.json"))
        if existing_lists:
            log(f"检测到已有提取缓存: {existing_lists[0]}，直接复用。")
            return output_dir

        if not self.token:
            raise ValueError("未检测到 MINERU_TOKEN，请在 .env 中配置 MinerU 平台 API 密钥！")

        log(f"开始向 MinerU 平台申请上传凭证: {pdf_name} ...")
        # 1. 申请上传凭证
        batch_url = f"{MINERU_API_BASE}/file-urls/batch"
        payload = {"files": [{"name": pdf_name}]}
        resp = requests.post(batch_url, headers=self.headers, json=payload, timeout=30)
        if resp.status_code != 200:
            raise RuntimeError(f"请求 MinerU 上传凭证失败 (状态码 {resp.status_code}): {resp.text}")
        
        res_json = resp.json()
        if res_json.get("code") != 0:
            raise RuntimeError(f"MinerU 业务错误: {res_json.get('msg', res_json)}")

        batch_id = res_json["data"]["batch_id"]
        file_urls = res_json["data"].get("file_urls", [])
        if not file_urls:
            raise RuntimeError(f"MinerU 返回的上传链接为空: {res_json}")

        upload_url = file_urls[0] if isinstance(file_urls[0], str) else file_urls[0].get("upload_url", file_urls[0].get("url"))
        
        log(f"成功获取 batch_id={batch_id}，正在上传文件流 ({os.path.getsize(pdf_path) / 1024 / 1024:.2f} MB)...")
        # 2. 上传文件内容
        with open(pdf_path, "rb") as f:
            put_resp = requests.put(upload_url, data=f, timeout=120)
            if put_resp.status_code not in [200, 201]:
                raise RuntimeError(f"上传 PDF 文件至存储桶失败 (状态码 {put_resp.status_code}): {put_resp.text}")

        log("文件上传成功，正在等待 MinerU UniMERNet 智能版面与公式提取...")
        # 3. 轮询结果
        query_url = f"{MINERU_API_BASE}/extract-results/batch/{batch_id}"
        poll_count = 0
        while True:
            time.sleep(4)
            poll_count += 1
            q_resp = requests.get(query_url, headers=self.headers, timeout=30)
            if q_resp.status_code != 200:
                continue
            q_data = q_resp.json()
            extract_result = q_data.get("data", {}).get("extract_result", [])
            if not extract_result:
                continue
            
            item = extract_result[0]
            state = item.get("state")
            if poll_count % 3 == 0:
                log(f"提取任务状态: {state} ...")

            if state == "done":
                zip_url = item.get("full_zip_url")
                if not zip_url:
                    raise RuntimeError("MinerU 提取成功但未提供 zip 下载链接！")
                log("提取完成！正在下载结构化成果包...")
                # 4. 下载 zip 并解压
                zip_path = os.path.join(output_dir, "result.zip")
                r_zip = requests.get(zip_url, timeout=180)
                with open(zip_path, "wb") as zf:
                    zf.write(r_zip.content)
                with zipfile.ZipFile(zip_path, 'r') as zf:
                    zf.extractall(output_dir)
                log(f"解压完成，提取目录就绪: {output_dir}")
                return output_dir
            elif state in ["failed", "error"]:
                raise RuntimeError(f"MinerU 提取任务执行失败: {item.get('err_msg', '未知错误')}")


def assemble_mineru_markdown(extracted_dir: str, start_page: int = 1) -> Tuple[str, Dict[str, str]]:
    """
    基于 MinerU 识别的 content_list.json 结构化数据，
    按自然阅读流装配段落与公式，生成嵌入【原书页码徽标】的 Markdown，
    并提取公式指纹到原图的映射表。
    """
    cl_files = glob.glob(os.path.join(extracted_dir, "*content_list*.json"))
    eq_img_map = {}

    if not cl_files:
        full_md_path = os.path.join(extracted_dir, "full.md")
        if os.path.exists(full_md_path):
            with open(full_md_path, "r", encoding="utf-8") as f:
                return f.read(), eq_img_map
        return "", eq_img_map

    with open(cl_files[0], "r", encoding="utf-8") as f:
        data = json.load(f)

    # 扫描真实印刷页码
    page_num_map = {}
    for b in data:
        if b.get("type") == "page_number" and b.get("text"):
            page_num_map[b.get("page_idx")] = b.get("text").strip()

    pieces = []
    current_page_idx = -1

    for b in data:
        p_idx = b.get("page_idx", -1)
        b_type = b.get("type", "")

        # 换页锚点
        if p_idx != current_page_idx and p_idx >= 0:
            current_page_idx = p_idx
            disp_page = page_num_map.get(p_idx, str(start_page + p_idx))
            marker = f'\n\n<div class="page-marker" id="page-{disp_page}"><span class="page-badge">── 原文第 {disp_page} 页 (Page {disp_page}) ──</span></div>\n\n'
            pieces.append(marker)

        # 过滤页眉页脚
        if b_type in ["header", "footer", "page_number", "page_footnote"]:
            continue

        if b_type == "text":
            level = b.get("text_level", 0)
            text = b.get("text", "").strip()
            if text:
                if level and level in [1, 2, 3, 4, 5]:
                    pieces.append(f"\n\n{'#' * level} {text}\n\n")
                else:
                    pieces.append(f"\n\n{text}\n\n")

        elif b_type == "equation":
            text = b.get("text", "").strip()
            img_path = b.get("img_path", "")
            if text:
                fp = formula_fingerprint(text)
                if fp and img_path:
                    # 统一为相对于产物目录的相对路径
                    eq_img_map[fp] = os.path.join("images", os.path.basename(img_path)).replace("\\", "/")
                pieces.append(f"\n\n$$\n{text}\n$$\n\n")

        elif b_type == "image":
            img_path = b.get("img_path", "")
            caption = b.get("image_title", "") or b.get("caption", "")
            if img_path:
                rel_img = os.path.join("images", os.path.basename(img_path)).replace("\\", "/")
                pieces.append(f"\n\n![{caption}]({rel_img})\n\n")

        elif b_type == "table":
            table_body = b.get("table_body", "") or b.get("text", "")
            if table_body:
                pieces.append(f"\n\n{table_body}\n\n")

    full_text = "".join(pieces)
    return full_text, eq_img_map
