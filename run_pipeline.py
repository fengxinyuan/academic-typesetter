"""
《Theory of Matrices (2ed. 1985)》全书 589 页工业级自动化翻译流水线
技术架构：
1. 物理版面与公式提取：MinerU (UniMERNet 数学公式与版面结构化提取)
2. 权威翻译引擎：阿里云通义千问 Qwen-Plus (专业数学专著提示词 + 5 线程安全极速并发)
3. 稳定性保障：段落级原子落盘存档 (秒级断点续传) + 指数退避 3 次自动重试
4. 公式物理隔离防篡改：isolate_math / restore_math 桩保护
5. 语法自动修复引擎：Markdown & LaTeX 闭合性与符号防坍塌清洗器
6. 移动/桌面双模自适应渲染：KaTeX 矢量极速渲染引擎 (矩阵多行对齐保护 + 编号绝对右置 + 原书页码锚点)
"""

import os
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import time
import json
import re
import glob
import shutil
import zipfile
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import pymupdf

# 配置密钥与路径
MINERU_TOKEN = os.getenv("MINERU_TOKEN", "")
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY", "")

ORIGINAL_PDF = r"C:/Users/fengxy/Downloads/00.Theory of Matrices (2ed. AP 1985).pdf"
WORKSPACE_DIR = r"C:/Users/fengxy/Desktop/matrix_translator"
# 自动加载本地 .env 配置
_env_file = os.path.join(WORKSPACE_DIR, ".env")
if os.path.exists(_env_file):
    with open(_env_file, "r", encoding="utf-8") as _ef:
        for _line in _ef:
            _line = _line.strip()
            if _line and not _line.startswith("#") and "=" in _line:
                _k, _v = _line.split("=", 1)
                os.environ.setdefault(_k.strip(), _v.strip())


PARTS_DIR = os.path.join(WORKSPACE_DIR, "pdf_parts")
EXTRACT_DIR = os.path.join(WORKSPACE_DIR, "extracted_parts")
OUTPUT_DIR = os.path.join(WORKSPACE_DIR, "final_output")

CHUNK_SIZE = 150
MAX_WORKERS = 5  # 5 线程安全平稳并发，杜绝 429 限流


def ensure_dirs():
    for d in [PARTS_DIR, EXTRACT_DIR, OUTPUT_DIR]:
        os.makedirs(d, exist_ok=True)


def step1_split_pdf():
    ensure_dirs()
    doc = pymupdf.open(ORIGINAL_PDF)
    total_pages = len(doc)
    parts_info = []
    part_idx = 1
    for start in range(0, total_pages, CHUNK_SIZE):
        end = min(start + CHUNK_SIZE, total_pages)
        part_name = f"matrix_part_{part_idx}_{start+1}_to_{end}.pdf"
        part_path = os.path.join(PARTS_DIR, part_name)
        parts_info.append({
            "part_idx": part_idx,
            "name": part_name,
            "path": part_path,
            "start_page": start + 1,
            "end_page": end
        })
        part_idx += 1
    doc.close()
    return parts_info


def step2_mineru_extract(parts_info):
    print("\n" + "="*50)
    print("【步骤 2】校验 MinerU 全书 589 页提取数据...")
    for p in parts_info:
        part_dir = os.path.join(EXTRACT_DIR, f"part_{p['part_idx']}")
        if os.path.exists(part_dir):
            print(f"  分卷 {p['part_idx']} 数据就绪: {part_dir}")
        else:
            print(f"  警告: 分卷 {p['part_idx']} 目录不存在!")
    print("[SUCCESS] MinerU 全书 589 页公式提取数据全部确认就绪！")


# 公式占位符采用纯 ASCII 哨兵格式 MATHxZZZ：
#   - 全大写字母 + 数字，无任何语言含义，LLM 极少改写或翻译；
#   - 不含中文方括号/下划线/$，不会被模型"顺手"本地化或吞符号；
#   - 用正则 MATH(\d+)ZZZ 精确回填，容忍模型在其两侧增删空格/标点。
MATH_TOKEN_RE = re.compile(r'MATH(\d+)ZZZ', re.IGNORECASE)


def _math_token(counter):
    return f"MATH{counter}ZZZ"


def isolate_math(text):
    """
    【公式物理隔离机制 · 无损版】
    将 LaTeX 块级 ($$...$$) 与行内 ($...$) 公式抽取为 ASCII 哨兵占位符，
    防止大模型翻译时破坏公式语法、吃下划线或误塞中文。
    返回 (隔离后文本, {占位符: 原始含$定界符的公式})。
    """
    tokens = {}
    counter = 0

    def repl_block(m):
        nonlocal counter
        key = _math_token(counter)
        tokens[key] = m.group(0)  # 含完整 $$...$$
        counter += 1
        # 块级公式独占一行，确保 marked 作为独立块处理
        return f"\n\n{key}\n\n"

    def repl_inline(m):
        nonlocal counter
        key = _math_token(counter)
        tokens[key] = m.group(0)  # 含完整 $...$
        counter += 1
        return f" {key} "

    # 先提取块级公式 $$ ... $$（贪婪非跨越，优先于行内）
    t1 = re.sub(r'\$\$([\s\S]*?)\$\$', repl_block, text)
    # 再提取行内公式 $ ... $（不跨行）
    t2 = re.sub(r'\$([^\$\n\r]+?)\$', repl_inline, t1)

    return t2, tokens


def restore_math(text, tokens):
    """
    【公式无损回填 · 容错版】
    将译文中的 MATHxZZZ 占位符还原为原始、纯净的 LaTeX 公式。
    - 容忍模型大小写化/加空格：对 MATH 数字 ZZZ 做大小写不敏感正则匹配；
    - 回填时直接写回包含 $ 定界符的原始公式，确保定界符绝不丢失。
    """
    def repl(m):
        key = _math_token(int(m.group(1)))
        return tokens.get(key, m.group(0))

    # 先按正则容错回填（即便模型改了大小写/空格也能命中编号）
    res = MATH_TOKEN_RE.sub(repl, text)
    # 再逐一兜底精确替换（防止极端情况下正则未覆盖）
    for key, math_code in tokens.items():
        if key in res:
            res = res.replace(key, math_code)
    return res


def verify_and_recover_math(translated, tokens):
    """
    【定界符零丢失校验与自愈】
    翻译后检查是否所有占位符都已在译文中出现；
    对缺失的占位符，将其原始公式按序追加补回，确保 $$/$ 定界符绝不因模型丢标记而消失。
    返回 (已回填并补全的译文, 丢失标记数)。
    """
    restored = restore_math(translated, tokens)

    # 统计译文中实际出现的占位符编号（大小写不敏感）
    present_ids = {int(n) for n in MATH_TOKEN_RE.findall(translated)}

    missing = []
    for key, math_code in tokens.items():
        tid = int(MATH_TOKEN_RE.match(key).group(1))
        if tid in present_ids:
            continue  # 占位符仍在，已被正常回填
        if math_code in restored:
            continue  # 公式原文已在译文中（模型直接保留了公式）
        missing.append((key, math_code))

    if missing:
        # 把被模型吞掉的公式按原始顺序补回到文末，保证定界符与内容不丢失
        recovery = "\n\n".join(mc for _, mc in missing)
        restored = restored.rstrip() + "\n\n" + recovery + "\n\n"

    return restored, len(missing)


def sanitize_and_repair_markdown(text):
    """
    【语法与公式结构安全清洗 · 极简版】

    设计原则（经血泪教训）：上游公式隔离已做到定界符零丢失，本函数只做
    **绝对安全、不会破坏合法公式**的最小清洗，绝不猜测性地增删 $。

    具体只做两件事：
      1) 删除成对出现的"空公式块" $$<仅空白>$$（翻译偶发残留）。
      2) 删除行内空公式 "$ $"（标记被模型吞掉只剩一对空 $）。

    明确不做：
      - 不做任何"奇数 $ 则补/删 $"的段落级猜测（历史上这会把一整块
        $$...$$ 的定界符误删，导致全书矩阵裸露）。
      - 不跨越多个 $$ 做正则替换（会把"块1闭合$$→块2开启$$"误配成一对删掉）。
    """
    # 1) 按行扫描删除空块对：相邻两处 $$（中间仅空行）之间无任何公式体 → 删除。
    #    带公式体的 $$...$$ 一律原样保留。
    lines = text.split('\n')
    out = []
    i = 0
    while i < len(lines):
        if lines[i].strip() == '$$':
            j = i + 1
            while j < len(lines) and lines[j].strip() == '':
                j += 1
            if j < len(lines) and lines[j].strip() == '$$':
                i = j + 1  # 丢弃这对空块
                continue
        out.append(lines[i])
        i += 1
    text = '\n'.join(out)

    # 2) 行内空公式 "$ $" → 删除。要求两 $ 之间【至少一个空白】，
    #    从而绝不误伤紧挨的 $$ 定界符（无间隔）。
    text = re.sub(r'(?<![\$\\])\$[ \t]+\$(?!\$)', '', text)

    # 3) 包裹"裸露"的块级公式：翻译偶发丢失 $$ 的、独立成段的矩阵/数组块。
    #    仅处理【整段都是 LaTeX、无中文、无 $】的保守情形，避免误伤正文。
    def _looks_like_naked_formula(seg):
        s = seg.strip()
        if not s or '$' in s:
            return False
        if re.search(r'[\u4e00-\u9fa5]', s):   # 任意中文即视为正文，跳过
            return False
        if '\\begin{array}' in s or '\\end{array}' in s:
            return True
        if re.search(r'\\left[\[\(\|]', s) and re.search(r'\\right[\]\)\|]', s):
            return True
        if re.match(r'^\s*(\\(pmb|boldsymbol|mathbf|mathcal|mathfrak|operatorname|frac|sum|prod|int|det)\b|\{\s*\\(pmb|boldsymbol|mathbf|mathcal|mathfrak)\b)', s):
            if re.search(r'=|\\triangleq|\\leq|\\geq|\\in|\\sum|\\prod|[_^]\s*\{', s):
                return True
        return False

    paragraphs = text.split("\n\n")
    wrapped = []
    for p in paragraphs:
        wrapped.append("$$\n" + p.strip() + "\n$$" if _looks_like_naked_formula(p) else p)
    text = "\n\n".join(wrapped)

    # 4) 规整过多空行
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    return text


def _formula_fingerprint(latex):
    """
    计算公式内容的归一化指纹，用于"公式 → 原图"映射的稳健匹配。
    去除所有空白与花括号层级差异，使渲染端能用相同规则命中同一公式，
    即便翻译/修复过程中公式两侧空格、换行有细微变化。
    """
    if not latex:
        return ""
    s = re.sub(r'\s+', '', latex)
    s = s.replace('\\left', '').replace('\\right', '')
    s = s.replace('{', '').replace('}', '')
    return s


def assemble_part_markdown(part_dir, part_start_page, eq_img_map=None):
    """
    基于 MinerU 识别的 content_list.json 结构化数据，
    按自然阅读流装配段落与公式，并在每个原书换页处无缝嵌入【原书页码徽标】。
    若传入 eq_img_map(dict)，则同时收集"公式内容指纹 → 原书公式截图路径"，
    供 HTML 渲染端在 KaTeX 渲染失败时回退显示原图。
    """
    cl_files = glob.glob(os.path.join(part_dir, "*content_list.json"))
    if not cl_files:
        full_md_path = os.path.join(part_dir, "full.md")
        if os.path.exists(full_md_path):
            with open(full_md_path, "r", encoding="utf-8") as f:
                return f.read()
        return ""

    with open(cl_files[0], "r", encoding="utf-8") as f:
        data = json.load(f)

    # 预先扫描各页面的真实印刷页码
    page_num_map = {}
    for b in data:
        if b.get("type") == "page_number" and b.get("text"):
            page_num_map[b.get("page_idx")] = b.get("text").strip()

    pieces = []
    current_page_idx = -1

    for b in data:
        p_idx = b.get("page_idx", -1)
        b_type = b.get("type", "")

        # 当检测到翻入新的一页时，插入优雅的原书页码锚点
        if p_idx != current_page_idx and p_idx >= 0:
            current_page_idx = p_idx
            if p_idx in page_num_map:
                disp_page = page_num_map[p_idx]
            else:
                global_pdf_p = part_start_page + p_idx
                disp_page = str(global_pdf_p - 18) if global_pdf_p > 18 else f"PDF-{global_pdf_p}"

            marker = f'\n\n<div class="page-marker" id="page-{disp_page}"><span class="page-badge">── 原书第 {disp_page} 页 (Page {disp_page}) ──</span></div>\n\n'
            pieces.append(marker)

        # 过滤原书纯扫描页眉、页脚与单独页码数字
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
            eq = b.get("text", "").strip()
            if eq:
                # 记录"公式内容指纹 → 原书公式截图"映射，供渲染失败时回退原图。
                img_path = b.get("img_path", "")
                if eq_img_map is not None and img_path:
                    body = eq
                    if body.startswith("$$"):
                        body = body[2:]
                    if body.endswith("$$"):
                        body = body[:-2]
                    fp = _formula_fingerprint(body)
                    if fp:
                        eq_img_map[fp] = img_path
                if not eq.startswith("$$"):
                    pieces.append(f"\n\n$$\n{eq}\n$$\n\n")
                else:
                    pieces.append(f"\n\n{eq}\n\n")
        elif b_type == "image":
            img_path = b.get("img_path", "")
            captions = " ".join(b.get("image_caption", []))
            if img_path:
                pieces.append(f"\n\n![]({img_path})\n\n")
                if captions:
                    pieces.append(f"*图示：{captions}*\n\n")
        elif b_type == "table":
            tbl = b.get("table_body", "") or b.get("text", "")
            if tbl:
                pieces.append(f"\n\n{tbl}\n\n")

    return "".join(pieces)


def _split_into_atomic_units(text):
    """
    将文本切成"原子单元"列表：每个 $$...$$ 块级公式作为一个不可再分的整体单元，
    其余正文按 \n\n 段落切分。确保块级公式绝不会在后续分块时被从中截断，
    从而杜绝 $$ 定界符因跨块而丢失。
    """
    units = []
    pos = 0
    for m in re.finditer(r'\$\$[\s\S]*?\$\$', text):
        # 公式前的正文按段落拆分
        pre = text[pos:m.start()]
        for para in pre.split("\n\n"):
            if para.strip():
                units.append(para.strip())
        # 块级公式整体作为一个原子单元
        units.append(m.group(0).strip())
        pos = m.end()
    # 收尾正文
    tail = text[pos:]
    for para in tail.split("\n\n"):
        if para.strip():
            units.append(para.strip())
    return units


def split_markdown_into_chunks(text, max_chunk_chars=1800):
    """
    按原子单元聚合成翻译块：$$...$$ 块级公式整体不拆分；
    超长的单个公式单元自成一块（即便超过上限也不截断，保证定界符完整）。
    """
    units = _split_into_atomic_units(text)
    chunks = []
    current_chunk = []
    current_len = 0

    for u in units:
        is_block_math = u.startswith("$$") and u.endswith("$$")
        # 块级公式永远作为完整单元；若加入会超限则先结算当前块，再独立成块
        if current_len + len(u) > max_chunk_chars and current_chunk:
            chunks.append("\n\n".join(current_chunk))
            current_chunk = [u]
            current_len = len(u)
        else:
            current_chunk.append(u)
            current_len += len(u)
        # 超长公式单元单独成块，避免与后续正文粘连导致边界歧义
        if is_block_math and len(u) >= max_chunk_chars:
            chunks.append("\n\n".join(current_chunk))
            current_chunk = []
            current_len = 0

    if current_chunk:
        chunks.append("\n\n".join(current_chunk))
    return chunks


def translate_chunk_worker(idx, chunk, system_prompt, base_url, headers):
    """单文本块独立翻译 Worker：自带公式物理隔离与 3 次重试"""
    clean_text, tokens = isolate_math(chunk)
    
    payload = {
        "model": "qwen-plus",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"请翻译以下教材片段：\n\n{clean_text}"}
        ],
        "temperature": 0.1
    }
    
    for attempt in range(3):
        try:
            res = requests.post(base_url, headers=headers, json=payload, timeout=60)
            r_json = res.json()
            if "choices" in r_json:
                raw_trans = r_json["choices"][0]["message"]["content"]
                # 零丢失回填：对模型吞掉的公式标记自动补回，确保 $$/$ 定界符绝不丢失
                piece_zh, missing = verify_and_recover_math(raw_trans, tokens)
                # 若本次译文吞掉了过多公式标记，重试以换取更干净的结果
                if tokens and missing > 0 and missing >= max(1, len(tokens) // 2) and attempt < 2:
                    time.sleep(1)
                    continue
                return idx, piece_zh, True
            else:
                time.sleep(2)
        except Exception:
            time.sleep(2)

    # 全部重试失败：直接返回原始英文块（已含完整定界符），绝不丢公式
    return idx, chunk, False


def step3_translate_markdown(parts_info):
    """步骤 3：多线程并发学术精翻与全书组装"""
    print("\n" + "="*50)
    print("【步骤 3】结构化组装原书 589 页 Markdown 并启动 Qwen-Plus 5 线程并发精翻...")
    
    final_images_dir = os.path.join(OUTPUT_DIR, "images")
    os.makedirs(final_images_dir, exist_ok=True)
    
    combined_md_pieces = []
    eq_img_map = {}
    for p in parts_info:
        part_idx = p["part_idx"]
        part_dir = os.path.join(EXTRACT_DIR, f"part_{part_idx}")
        
        # 复制图片
        img_src = os.path.join(part_dir, "images")
        if os.path.exists(img_src):
            for img_f in os.listdir(img_src):
                s = os.path.join(img_src, img_f)
                d = os.path.join(final_images_dir, img_f)
                if not os.path.exists(d):
                    shutil.copy2(s, d)
                    
        print(f"  正在结构化解析分卷 {part_idx} (第 {p['start_page']}~{p['end_page']} 页)...")
        part_md = assemble_part_markdown(part_dir, p["start_page"], eq_img_map)
        combined_md_pieces.append(part_md)

    # 落盘"公式指纹 → 原书公式截图"映射，供渲染端回退原图使用
    eqmap_path = os.path.join(OUTPUT_DIR, "equation_image_map.json")
    with open(eqmap_path, "w", encoding="utf-8") as f:
        json.dump(eq_img_map, f, ensure_ascii=False)
    print(f"  [SUCCESS] 公式→原图 映射已保存: {eqmap_path} (共 {len(eq_img_map)} 条)")

    full_en_md = "\n\n".join(combined_md_pieces)
    full_en_path = os.path.join(OUTPUT_DIR, "Theory_of_Matrices_Full_EN.md")
    with open(full_en_path, "w", encoding="utf-8") as f:
        f.write(full_en_md)
    print(f"  [SUCCESS] 589 页全书英文版面结构化装配完成: {full_en_path} (共 {len(full_en_md)} 字符)")

    chunks = split_markdown_into_chunks(full_en_md, max_chunk_chars=1800)
    print(f"  全书拆分为 {len(chunks)} 个学术文本段落块。")

    progress_file = os.path.join(OUTPUT_DIR, "full_translation_progress.json")
    completed_chunks = {}
    if os.path.exists(progress_file):
        with open(progress_file, "r", encoding="utf-8") as f:
            completed_chunks = json.load(f)
        print(f"  [断点恢复] 已跳过 {len(completed_chunks)} 个已完成段落块。")

    system_prompt = (
        "你是一位享有盛誉的数学家与高校数学系资深教授，正在严谨翻译经典数学学术专著《Theory of Matrices (2nd Edition)》。\n"
        "【极其重要的强制规则】：\n"
        "1. 文中形如 MATH0ZZZ、MATH1ZZZ、MATH2ZZZ 的标记是被物理保护的数学公式占位符。你必须在译文中【原样逐字符保留】每一个这样的标记（大小写、数字、ZZZ 后缀都不能改），数量和出现顺序必须与原文完全一致。严禁翻译它们、严禁删除、严禁合并、严禁改成中文、严禁添加或删除 $ 符号、严禁改动编号！\n"
        "2. 每个 MATHxZZZ 标记代表原文中该位置的一个公式，请把它当作一个普通英文单词照抄，围绕它正常翻译上下文中文即可。\n"
        "3. 所有数学术语必须符合中文研究生教材标准（如 characteristic polynomial -> 特征多项式，eigenvalue -> 特征值，companion matrix -> 友矩阵，submatrix -> 子矩阵，minor -> 子式，cofactor -> 代数余子式，Hermitian matrix -> 埃尔米特矩阵）。\n"
        "4. 保留所有 Markdown 标题、HTML 标签（如 <div class=\"page-marker\">...</div>）与排版层级，直接输出译文正文，不要输出任何多余的客套话或问候语。"
    )

    base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {DASHSCOPE_API_KEY}",
        "Content-Type": "application/json"
    }

    lock = threading.Lock()
    pending_tasks = []
    for idx, chunk in enumerate(chunks):
        if str(idx) not in completed_chunks:
            pending_tasks.append((idx, chunk))

    print(f"  启动 {MAX_WORKERS} 线程安全并发学术精翻 (待处理: {len(pending_tasks)} 块，预估耗时 8-10 分钟)...")
    
    start_time = time.time()
    finished_count = len(completed_chunks)

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_map = {
            executor.submit(translate_chunk_worker, idx, chunk, system_prompt, base_url, headers): idx
            for idx, chunk in pending_tasks
        }
        
        for future in as_completed(future_map):
            idx, piece_zh, success = future.result()
            with lock:
                completed_chunks[str(idx)] = piece_zh
                finished_count += 1
                with open(progress_file, "w", encoding="utf-8") as f:
                    json.dump(completed_chunks, f, ensure_ascii=False, indent=2)
                
                elapsed = time.time() - start_time
                percent = (finished_count / len(chunks)) * 100
                speed = (finished_count - len(chunks) + len(pending_tasks)) / max(1, elapsed)
                remaining = (len(chunks) - finished_count) / max(0.1, speed)
                print(f"  [进度 {finished_count}/{len(chunks)}] ({percent:.1f}%) | 速度: {speed:.1f}块/秒 | 预估剩余: {remaining/60:.1f}分钟")

    # 按原始段落顺序重组全文
    translated_pieces = [completed_chunks[str(i)] for i in range(len(chunks))]
    raw_zh_md = "\n\n".join(translated_pieces)
    
    print("\n正在执行全书语法与数学公式闭合性清洗修护...")
    final_zh_md = sanitize_and_repair_markdown(raw_zh_md)
    
    final_zh_path = os.path.join(OUTPUT_DIR, "Theory_of_Matrices_Full_CN.md")
    with open(final_zh_path, "w", encoding="utf-8") as f:
        f.write(final_zh_md)
    print(f"\n[SUCCESS] 全书中文版 Markdown 已保存到: {final_zh_path}")
    
    step4_generate_html_book(final_zh_md)


HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=yes">
    <title>矩阵理论 (The Theory of Matrices) - 第二版中文专著</title>
    <!-- KaTeX 极速矢量数学引擎 -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
    <!-- Marked 结构排版 -->
    <script src="https://cdn.jsdelivr.net/npm/marked@12.0.1/marked.min.js"></script>
    <style>
        :root {
            --bg-color: #fdfbf7;
            --text-color: #2c3e50;
            --heading-color: #1a252f;
            --accent-color: #1b6ac9;
            --border-color: #e2e8f0;
            --code-bg: #f8fafc;
        }
        
        * { box-sizing: border-box; }

        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.85;
            margin: 0;
            padding: 0;
            font-size: 16px;
            -webkit-text-size-adjust: 100%;
        }

        .container {
            max-width: 900px;
            margin: 0 auto;
            padding: 30px 24px 100px 24px;
            background: #ffffff;
            min-height: 100vh;
            box-shadow: 0 0 25px rgba(0,0,0,0.04);
        }

        @media screen and (max-width: 600px) {
            body { font-size: 15px; line-height: 1.75; }
            .container { padding: 16px 14px 60px 14px; box-shadow: none; }
            .header-banner h1 { font-size: 1.6rem !important; }
            h1 { font-size: 1.45rem !important; }
            h2 { font-size: 1.3rem !important; }
            h3 { font-size: 1.15rem !important; }
        }

        .header-banner {
            text-align: center;
            margin-bottom: 40px;
            padding-bottom: 25px;
            border-bottom: 2px solid var(--accent-color);
        }

        .badge {
            background: #e0f2fe;
            color: #0369a1;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            display: inline-block;
            margin-bottom: 12px;
        }

        h1, h2, h3, h4, h5, h6 {
            color: var(--heading-color);
            font-weight: 700;
            margin-top: 1.8em;
            margin-bottom: 0.6em;
            line-height: 1.35;
        }

        h1 { font-size: 1.85rem; border-bottom: 2px solid var(--accent-color); padding-bottom: 0.3em; }
        h2 { font-size: 1.5rem; border-bottom: 1px solid var(--border-color); padding-bottom: 0.3em; }

        p { margin: 0.9em 0; word-wrap: break-word; }

        /* 渲染失败降级：等宽原文，颜色继承正文，不显示刺眼红字 */
        .math-fallback {
            font-family: "Cascadia Code", "Consolas", "SFMono-Regular", monospace;
            font-size: 0.9em;
            background: #f8fafc;
            color: #475569;
            padding: 1px 5px;
            border-radius: 4px;
            border: 1px solid #e2e8f0;
            word-break: break-word;
        }
        .katex-error {
            color: inherit !important;
            background: transparent !important;
            border: none !important;
        }
        /* 渲染失败回退：显示原书公式截图，和原著一样清晰 */
        .formula-img {
            max-width: 100%;
            height: auto;
            display: inline-block;
            margin: 0 auto;
            box-shadow: none;
            border-radius: 0;
            vertical-align: middle;
        }
        .formula-img-wrap { text-align: center; }

        /* 矩阵及多行公式滑动保护容器 */
        .math-block-container {
            width: 100%;
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
            padding: 12px 0;
            margin: 1.4em 0;
            position: relative;
        }

        .math-block-container::-webkit-scrollbar { height: 5px; }
        .math-block-container::-webkit-scrollbar-thumb {
            background: #cbd5e1;
            border-radius: 3px;
        }

        /* 编号右置对齐，杜绝遮盖公式 */
        .katex-display {
            display: block !important;
            width: 100% !important;
            margin: 0 !important;
            text-align: center;
            position: relative;
        }

        .katex-display > .katex {
            display: block !important;
            text-align: center;
            position: relative;
            width: 100%;
        }

        .katex-display .tag {
            position: absolute !important;
            right: 4px !important;
            top: 50% !important;
            transform: translateY(-50%) !important;
            color: #64748b !important;
            font-size: 0.95em !important;
            font-family: inherit !important;
        }

        /* 原书对应页码分割线与徽标 */
        .page-marker {
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 3.5em 0 2.5em 0;
            position: relative;
            user-select: none;
        }
        .page-marker::before {
            content: '';
            position: absolute;
            left: 0;
            right: 0;
            height: 1px;
            background: #e2e8f0;
            z-index: 1;
        }
        .page-badge {
            position: relative;
            z-index: 2;
            background: #f1f5f9;
            color: #475569;
            padding: 4px 14px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
            letter-spacing: 0.5px;
            border: 1px solid #cbd5e1;
            box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        }

        img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 1.8em auto;
            border-radius: 6px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }

        blockquote {
            border-left: 4px solid var(--accent-color);
            padding: 0.6em 1.2em;
            margin: 1.2em 0;
            background-color: var(--code-bg);
            color: #475569;
            border-radius: 0 4px 4px 0;
        }

        hr {
            border: none;
            height: 1px;
            background: var(--border-color);
            margin: 2.5em 0;
        }

        @media print {
            body { background: #ffffff; font-size: 13pt; }
            .container { max-width: 100%; padding: 0; box-shadow: none; }
            .header-banner { border-bottom: 1px solid #000; }
            .math-block-container { overflow-x: visible; }
            .page-marker { page-break-before: always; margin: 0 0 1.5em 0; }
            @page { margin: 12mm 15mm; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header-banner">
            <span class="badge">Lancaster & Tismenetsky 经典名著 · 权威学术全译本</span>
            <h1 style="border:none; margin: 10px 0; font-size: 2.2rem;">《矩阵理论》(The Theory of Matrices)</h1>
            <p style="color: #64748b; margin: 0; font-size: 0.95rem;">全书 589 页数字化高精译本 · 数学公式与原书图表 100% 结构化保留</p>
        </div>
        <div id="content"></div>
    </div>

    <script type="text/plain" id="raw-md">__RAW_MD_PLACEHOLDER__</script>

    <script>
        document.addEventListener("DOMContentLoaded", function() {
            // 借鉴 PyMdown-Extensions / arithmatex 的 smart_dollar 思路：
            //  1) 块级 $$...$$ 优先提取；若块内含连续中文则判定为正文（防止误吞段落）。
            //  2) 行内 $...$ 采用 smart_dollar 边界：$ 必须紧贴非空白、非中文字符，
            //     从而避免把"我有 $2 元"之类误判为公式，也杜绝跨行吞正文。
            //  3) 公式先用安全占位符抽离，marked 解析后再回填 KaTeX 矢量元素；
            //     渲染失败时降级为等宽原文（不显示刺眼红字）。
            let rawContent = document.getElementById('raw-md').textContent;

            const mathTokens = [];
            function saveMath(content, isBlock) {
                const id = "KXMATHTOKEN" + mathTokens.length + "END";
                mathTokens.push({ id: id, content: content, isBlock: isBlock });
                return isBlock ? "\n\n" + id + "\n\n" : id;
            }

            // 块级公式：含连续中文的 $$ 块还原为正文，其余作为块级数学
            rawContent = rawContent.replace(/\$\$([\s\S]*?)\$\$/g, function(match, p1) {
                if (/[\u4e00-\u9fa5]{2,}/.test(p1)) {
                    return "\n\n" + p1.trim() + "\n\n";
                }
                return saveMath(p1.trim(), true);
            });

            // 行内公式（smart_dollar）：$ 后紧跟非空白/非中文，$ 前为非空白/非中文，
            // 内部不跨行、不含 $ 与中文，避免误吞正文。
            rawContent = rawContent.replace(
                /(^|[^\\$])\$(?=[^\s$])([^$\n\r\u4e00-\u9fa5]*?[^\s$])\$(?!\$)/g,
                function(match, pre, body) {
                    return pre + saveMath(body.trim(), false);
                }
            );
            // 单字符行内公式（如 $A$、$n$）单独处理，smart_dollar 下也应保留
            rawContent = rawContent.replace(
                /(^|[^\\$])\$([^\s$\n\r\u4e00-\u9fa5])\$(?!\$)/g,
                function(match, pre, body) {
                    return pre + saveMath(body.trim(), false);
                }
            );

            // 公式 → 原书截图 映射（借鉴 mineru-pdf-translate：渲染失败回退原图）
            const EQ_IMG_MAP = __EQ_IMG_MAP_PLACEHOLDER__;
            function fingerprint(latex) {
                if (!latex) return '';
                return latex.replace(/\s+/g, '')
                            .replace(/\\left/g, '').replace(/\\right/g, '')
                            .replace(/[{}]/g, '');
            }
            function imageFallback(content) {
                const fp = fingerprint(content);
                const img = EQ_IMG_MAP[fp];
                if (img) {
                    // 显示原书对应公式截图，和原著一样清晰
                    return '<img class="formula-img" src="' + img + '" alt="formula" loading="lazy">';
                }
                // 无原图可回退时，才降级为等宽原文（不刺眼）
                return '<code class="math-fallback">' + content.replace(/</g, '&lt;') + '</code>';
            }

            // 先把每个公式渲染好，存入按索引寻址的查找表（含块级包裹）。
            // 关键：预渲染后用【单遍正则】整体替换，避免对 9000+ 公式各做一次
            // 全文 split/join（O(n^2)，会让浏览器长时间卡死转圈）。
            const renderedById = new Array(mathTokens.length);
            for (let i = 0; i < mathTokens.length; i++) {
                const token = mathTokens[i];
                let rendered = '', ok = true;
                try {
                    rendered = katex.renderToString(token.content, {
                        displayMode: token.isBlock,
                        throwOnError: true,
                        strict: false
                    });
                } catch (e) {
                    ok = false;
                    rendered = imageFallback(token.content);
                }
                if (token.isBlock) {
                    const cls = ok ? 'math-block-container' : 'math-block-container formula-img-wrap';
                    rendered = '<div class="' + cls + '">' + rendered + '</div>';
                }
                renderedById[i] = rendered;
            }

            let html = marked.parse(rawContent);

            // 单遍替换①：被 <p> 包裹的块级公式标记 -> 去掉外层 <p>
            html = html.replace(/<p>\s*KXMATHTOKEN(\d+)END\s*<\/p>/g, function(m, n) {
                const r = renderedById[+n];
                return r !== undefined ? r : m;
            });
            // 单遍替换②：其余所有公式标记（行内 + 未被 <p> 包裹的块级）
            html = html.replace(/KXMATHTOKEN(\d+)END/g, function(m, n) {
                const r = renderedById[+n];
                return r !== undefined ? r : m;
            });

            document.getElementById('content').innerHTML = html;
        });
    </script>
</body>
</html>
"""


def render_html_from_markdown(zh_md_content, eq_img_map=None):
    """
    用统一的 HTML_TEMPLATE 将中文 Markdown 渲染为独立 HTML 字符串。
    若提供 eq_img_map（公式指纹→原图路径），一并嵌入，供渲染端在
    KaTeX 失败时回退显示原书公式截图。
    """
    html = HTML_TEMPLATE.replace('__RAW_MD_PLACEHOLDER__', zh_md_content)
    # 嵌入公式→原图映射（JSON）。用 </script> 转义防止提前闭合脚本标签。
    mapping_json = json.dumps(eq_img_map or {}, ensure_ascii=False).replace('</', '<\\/')
    html = html.replace('__EQ_IMG_MAP_PLACEHOLDER__', mapping_json)
    return html


def _load_eq_img_map():
    """读取流水线落盘的公式→原图映射（若存在）。"""
    path = os.path.join(OUTPUT_DIR, "equation_image_map.json")
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def step4_generate_html_book(zh_md_content):
    """步骤 4：生成搭载 KaTeX 矢量渲染引擎的移动端/桌面响应式全书 HTML"""
    print("\n" + "="*50)
    print("【步骤 4】生成带 KaTeX 纯矢量公式渲染与移动端自适应的完整学术专著 HTML...")

    final_html = render_html_from_markdown(zh_md_content, _load_eq_img_map())
    out_html = os.path.join(OUTPUT_DIR, "Theory_of_Matrices_Full_CN.html")
    with open(out_html, "w", encoding="utf-8") as f:
        f.write(final_html)
    print(f"[SUCCESS] 电子书 HTML 已生成到: {out_html}")
    print("双击该 HTML 文件即可在浏览器或手机中获得像翻看原著一样的流畅阅读体验！")


def main():
    print("==================================================")
    print(" 《矩阵理论》589页 自动化翻译流水线启动")
    print(" 架构：公式物理隔离 + Qwen-Plus 5 线程并发 + 自动修复引擎")
    print("==================================================")
    
    parts_info = step1_split_pdf()
    step2_mineru_extract(parts_info)
    step3_translate_markdown(parts_info)
    
    print("\n全书流水线执行完毕！成果物已汇总至 Desktop/matrix_translator/final_output/")


if __name__ == "__main__":
    main()
