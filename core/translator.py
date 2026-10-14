# -*- coding: utf-8 -*-
"""
统一学术翻译与大模型驱动器
内置公式哨兵隔离、术语表注入、多语言支持、原子级断点续传与并发重试。
"""

import os
import sys
import json
import time
import requests
from typing import List, Dict, Optional, Callable, Union
from concurrent.futures import ThreadPoolExecutor, as_completed

from core.config import (
    DASHSCOPE_API_KEY, DEEPSEEK_API_KEY, OPENAI_API_KEY, OPENAI_BASE_URL,
    get_default_model, DEFAULT_MAX_WORKERS
)
from core.sentinel import isolate_math, verify_and_recover_math, sanitize_and_repair_markdown


def build_system_prompt(target_lang: str = "zh-CN", 
                        domain: str = "academic", 
                        glossary: Optional[Dict[str, str]] = None,
                        custom_instructions: Optional[str] = None) -> str:
    """动态构建学术翻译 System Prompt，支持多语言、专业领域与自定义术语对齐"""
    
    lang_map = {
        "zh": "中文",
        "zh-cn": "中文 (简体)",
        "zh-tw": "中文 (繁体)",
        "en": "English",
        "ja": "日本語",
        "de": "Deutsch",
        "fr": "Français"
    }
    lang_name = lang_map.get(target_lang.lower(), target_lang)

    prompt_lines = [
        f"你是一位顶尖的国际学术期刊审稿专家与学术翻译家。",
        f"你的任务是将输入的学术文献（论文、专著、技术报告或讲义）翻译为严谨、权威、出版级的【{lang_name}】。",
        "",
        "【排版与公式保护核心准则】（必须严格遵守）：",
        "1. 绝对保真：严禁删减、总结、扩写或更改原文的论述逻辑与学术事实。",
        "2. 数学公式占位符绝对物理隔离：",
        "   - 文本中的 `MATH0ZZZ`、`MATH1ZZZ`、`MATH2ZZZ` 等是公式占位符；",
        "   - 严禁翻译、改写、拆分或删除任何 `MATHxZZZ` 占位符！",
        "   - 原文中的占位符必须 1:1、完整且原位保留在译文中对应的语法位置上。",
        "3. 学术规范：",
        f"   - 标点符号使用标准的目标语言标点（如翻译为中文时使用中文标点，除公式占位符两侧外）。",
        "   - 保留所有 Markdown 结构（标题 #、列表、引用 >）与 HTML 锚点标签（如 <div class=\"page-marker\"...）。",
    ]

    if domain == "math":
        prompt_lines.append("   - 定理、定义、引理、推论、例题、习题、证明等数学逻辑单元以加粗标题呈现（如 **定理 1.**、**证明.** 等）。")

    # 动态注入专业术语表
    if glossary:
        prompt_lines.append("")
        prompt_lines.append("【专属专业术语对照表】（必须严格统一采用）：")
        for k, v in glossary.items():
            prompt_lines.append(f"   - {k} -> {v}")

    if custom_instructions:
        prompt_lines.append("")
        prompt_lines.append("【用户附加要求】：")
        prompt_lines.append(f"   {custom_instructions}")

    prompt_lines.append("")
    prompt_lines.append("4. 纯净输出：直接输出排版翻译后的正文，严禁输出任何问候语、确认词、解释性文字，严禁在外层包裹 ```markdown 代码块！")

    return "\n".join(prompt_lines)


class AcademicTranslator:
    def __init__(self, 
                 model_name: Optional[str] = None, 
                 api_key: Optional[str] = None, 
                 base_url: Optional[str] = None,
                 target_lang: str = "zh-CN",
                 domain: str = "academic",
                 glossary: Optional[Union[Dict[str, str], str]] = None,
                 custom_system_prompt: Optional[str] = None):
        
        self.model_name = model_name or get_default_model()
        self.target_lang = target_lang
        self.domain = domain

        # 处理术语表
        if isinstance(glossary, str) and os.path.isfile(glossary):
            with open(glossary, "r", encoding="utf-8") as gf:
                self.glossary = json.load(gf)
        elif isinstance(glossary, dict):
            self.glossary = glossary
        else:
            self.glossary = None

        # 确定 API Key 与 Base URL
        if api_key:
            self.api_key = api_key
        elif "deepseek" in self.model_name.lower():
            self.api_key = DEEPSEEK_API_KEY or DASHSCOPE_API_KEY
        elif "qwen" in self.model_name.lower():
            self.api_key = DASHSCOPE_API_KEY
        else:
            self.api_key = OPENAI_API_KEY or DASHSCOPE_API_KEY

        if base_url:
            self.api_url = base_url
        elif "deepseek" in self.model_name.lower():
            self.api_url = "https://api.deepseek.com/v1/chat/completions"
        elif "qwen" in self.model_name.lower():
            self.api_url = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
        else:
            self.api_url = OPENAI_BASE_URL or "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"

        self.system_prompt = custom_system_prompt or build_system_prompt(
            target_lang=self.target_lang,
            domain=self.domain,
            glossary=self.glossary
        )

        if not self.api_key:
            raise ValueError(f"未检测到适用于模型 {self.model_name} 的 API 密钥，请在 .env 中设置相应 KEY！")

    def call_llm(self, prompt: str, system_prompt: Optional[str] = None, max_retries: int = 3, temperature: float = 0.1) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model_name,
            "messages": [
                {"role": "system", "content": system_prompt or self.system_prompt},
                {"role": "user", "content": prompt}
            ],
            "temperature": temperature
        }

        last_err = None
        for attempt in range(max_retries):
            try:
                resp = requests.post(self.api_url, headers=headers, json=payload, timeout=60)
                if resp.status_code == 200:
                    data = resp.json()
                    text = data['choices'][0]['message']['content'].strip()
                    if text.startswith("```markdown"):
                        text = text[11:].strip()
                    elif text.startswith("```"):
                        text = text[3:].strip()
                    if text.endswith("```"):
                        text = text[:-3].strip()
                    return text
                elif resp.status_code == 429:
                    time.sleep(2 * (attempt + 1))
                else:
                    last_err = f"HTTP {resp.status_code}: {resp.text}"
                    time.sleep(1.5)
            except Exception as e:
                last_err = str(e)
                time.sleep(2)

        raise RuntimeError(f"大模型调用失败 (重试 {max_retries} 次): {last_err}")

    def translate_segment(self, segment_text: str) -> str:
        """对单段文本执行公式隔离 -> 大模型翻译 -> 公式自愈与回填"""
        clean_text, tokens = isolate_math(segment_text)
        prompt = f"请翻译并格式化以下学术内容，严格保留所有 MATHxZZZ 占位符：\n\n{clean_text}"
        translated_raw = self.call_llm(prompt)
        restored, _ = verify_and_recover_math(translated_raw, tokens)
        return sanitize_and_repair_markdown(restored)

    def translate_document(self, 
                           markdown_text: str, 
                           progress_cache_path: str, 
                           max_workers: int = DEFAULT_MAX_WORKERS,
                           log_cb: Optional[Callable[[str], None]] = None) -> str:
        """
        全文档并发安全翻译调度器。
        支持切片级原子落盘存档，随时中断、随时秒级续跑。
        """
        def log(msg):
            if log_cb:
                log_cb(msg)
            else:
                print(f"[Translator] {msg}")

        # 切分逻辑块（以换页锚点或自然大段落切分）
        if '<div class="page-marker"' in markdown_text:
            raw_chunks = markdown_text.split('<div class="page-marker"')
            chunks = []
            for idx, chunk in enumerate(raw_chunks):
                if idx == 0:
                    if chunk.strip():
                        chunks.append(chunk)
                else:
                    chunks.append('<div class="page-marker"' + chunk)
        else:
            # 针对没有 page-marker 的通用文档，按二级/三级标题或双换行分段分块
            raw_sections = markdown_text.split("\n\n## ")
            chunks = []
            for idx, sec in enumerate(raw_sections):
                if idx == 0:
                    chunks.append(sec)
                else:
                    chunks.append("## " + sec)

        total_chunks = len(chunks)
        log(f"文档切片完成，共计 {total_chunks} 个逻辑块。")

        # 读取进度存档
        progress = {}
        if os.path.exists(progress_cache_path):
            try:
                with open(progress_cache_path, "r", encoding="utf-8") as pf:
                    progress = json.load(pf)
                log(f"已装载进度存档，已完成 {len(progress)}/{total_chunks} 块。")
            except Exception:
                progress = {}

        todo_indices = [i for i in range(total_chunks) if str(i) not in progress]
        if not todo_indices:
            log("所有切片已全部完成！直接合并装配。")
            return "\n\n".join(progress[str(i)] for i in range(total_chunks))

        log(f"启动 {max_workers} 线程并发处理...")

        def _worker(i):
            chunk_content = chunks[i]
            if len(chunk_content.strip()) < 30 and "page-marker" in chunk_content:
                return i, chunk_content
            res = self.translate_segment(chunk_content)
            return i, res

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_map = {executor.submit(_worker, i): i for i in todo_indices}
            done_count = len(progress)
            for future in as_completed(future_map):
                idx = future_map[future]
                try:
                    i, translated_part = future.result()
                    progress[str(i)] = translated_part
                    done_count += 1
                    with open(progress_cache_path, "w", encoding="utf-8") as pf:
                        json.dump(progress, pf, ensure_ascii=False)
                    if done_count % 5 == 0 or done_count == total_chunks:
                        log(f"进度: {done_count}/{total_chunks} ({(done_count/total_chunks)*100:.1f}%)")
                except Exception as e:
                    log(f"切片 {idx} 处理异常: {e}")

        return "\n\n".join(progress[str(i)] for i in range(total_chunks) if str(i) in progress)
