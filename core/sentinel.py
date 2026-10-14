# -*- coding: utf-8 -*-
"""
工业级数学公式哨兵隔离与自愈保护模块
核心价值：彻底防止大模型在翻译或排版时篡改公式、破坏下划线、吞噬符号或翻译数学变量。
"""

import re

MATH_TOKEN_RE = re.compile(r'MATH(\d+)ZZZ', re.IGNORECASE)

def _math_token(counter: int) -> str:
    return f"MATH{counter}ZZZ"

def isolate_math(text: str):
    """
    【公式物理隔离机制 · 无损版】
    将 LaTeX 块级 ($$...$$) 与行内 ($...$) 公式抽取为 ASCII 哨兵占位符 MATHxZZZ。
    返回: (隔离后文本, {占位符: 原始含$定界符的公式})
    """
    tokens = {}
    counter = 0

    def repl_block(m):
        nonlocal counter
        key = _math_token(counter)
        tokens[key] = m.group(0)  # 含完整 $$...$$
        counter += 1
        return f"\n\n{key}\n\n"

    def repl_inline(m):
        nonlocal counter
        key = _math_token(counter)
        tokens[key] = m.group(0)  # 含完整 $...$
        counter += 1
        return f" {key} "

    # 先提取块级公式 $$ ... $$
    t1 = re.sub(r'\$\$([\s\S]*?)\$\$', repl_block, text)
    # 再提取行内公式 $ ... $
    t2 = re.sub(r'(?<!\$)\$(?!\$)([^\$\n\r]+?)(?<!\$)\$(?!\$)', repl_inline, t1)

    return t2, tokens

def restore_math(text: str, tokens: dict) -> str:
    """
    【公式无损回填 · 容错版】
    将译文中的 MATHxZZZ 占位符还原为原始的 LaTeX 公式。
    """
    def repl(m):
        key = _math_token(int(m.group(1)))
        return tokens.get(key, m.group(0))

    res = MATH_TOKEN_RE.sub(repl, text)
    # 兜底精确替换
    for key, math_code in tokens.items():
        if key in res:
            res = res.replace(key, math_code)
    return res

def verify_and_recover_math(translated: str, tokens: dict):
    """
    【定界符零丢失校验与自愈】
    检查模型是否吞掉了某些公式；若吞掉，按顺序在末尾补齐，保证无损。
    返回: (已回填补全的译文, 丢失标记数)
    """
    restored = restore_math(translated, tokens)
    present_ids = {int(n) for n in MATH_TOKEN_RE.findall(translated)}

    missing = []
    for key, math_code in tokens.items():
        m = MATH_TOKEN_RE.match(key)
        if m:
            tid = int(m.group(1))
            if tid in present_ids:
                continue
        if math_code in restored:
            continue
        missing.append((key, math_code))

    if missing:
        recovery = "\n\n".join(mc for _, mc in missing)
        restored = restored.rstrip() + "\n\n" + recovery + "\n\n"

    return restored, len(missing)

def sanitize_and_repair_markdown(text: str) -> str:
    """
    【语法与公式结构安全清洗】
    1) 剔除空公式块 $$ $$
    2) 剔除行内空公式 $ $
    3) 保守包裹裸露的 LaTeX 块级矩阵环境 (\begin{array}, \begin{bmatrix} 等)
    4) 规范连续空行
    """
    # 1) 按行扫描删除空块对
    lines = text.split('\n')
    out = []
    i = 0
    while i < len(lines):
        if lines[i].strip() == '$$':
            j = i + 1
            while j < len(lines) and lines[j].strip() == '':
                j += 1
            if j < len(lines) and lines[j].strip() == '$$':
                i = j + 1
                continue
        out.append(lines[i])
        i += 1
    text = '\n'.join(out)

    # 2) 行内空公式
    text = re.sub(r'(?<![\$\\])\$[ \t]+\$(?!\$)', '', text)

    # 3) 裸露矩阵或公式安全包裹
    def _looks_like_naked_formula(seg: str) -> bool:
        s = seg.strip()
        if not s or '$' in s:
            return False
        if re.search(r'[\u4e00-\u9fa5]', s):
            return False
        if '\\begin{array}' in s or '\\begin{matrix}' in s or '\\begin{pmatrix}' in s or '\\begin{bmatrix}' in s:
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

def formula_fingerprint(latex: str) -> str:
    """计算公式归一化指纹，用于 KaTeX 渲染失败时回退原图匹配"""
    if not latex:
        return ""
    s = re.sub(r'\s+', '', latex)
    s = s.replace('\\left', '').replace('\\right', '')
    s = s.replace('{', '').replace('}', '')
    return s
