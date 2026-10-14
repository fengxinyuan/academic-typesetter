# -*- coding: utf-8 -*-
"""
出版级学术排版与自愈引擎
支持可配置的学术卡片（定理、定义、算法、例题、证明等）与单页物理词法自愈。
"""

import os
import re
from typing import Optional, List, Dict, Tuple
from core.translator import AcademicTranslator

# 默认支持的中英双语学术卡片配置: (关键词正则列表, CSS 类名, 卡片类型)
DEFAULT_CARD_RULES: List[Tuple[List[str], str, str]] = [
    (["定理", "Theorem"], "card-theorem", "定理"),
    (["定义", "Definition"], "card-definition", "定义"),
    (["引理", "推论", "命题", "Lemma", "Corollary", "Proposition"], "card-lemma", "引理/推论"),
    (["算法", "伪代码", "Algorithm", "Pseudocode"], "card-algorithm", "算法"),
    (["例", "例题", "Example"], "card-example", "例题"),
    (["习题", "思考题", "练习", "Exercise", "Problem"], "card-exercise", "习题"),
    (["证明", "Proof"], "card-proof", "证明"),
    (["注", "备注", "说明", "Remark", "Note"], "card-remark", "备注"),
]


class PageHealer:
    """单页大模型自愈排版器：实现单页词法隔离，杜绝跨页定界符雪崩"""
    def __init__(self, translator: Optional[AcademicTranslator] = None):
        self.translator = translator or AcademicTranslator()

    def heal_page(self, page_content: str, language_hint: str = "zh") -> str:
        sys_prompt = f"""你是一位顶尖的学术专著与 LaTeX 排版专家。你的任务是对学术文献的单页内容进行出版级排版与数学公式精校。

【排版精校准则】：
1. 绝对保真：严禁删减、总结、扩写或更改原文的论述逻辑。保留任何 `<div class="page-marker" ...>` 标签。
2. 根除公式源码裸露与定界符错位：
   - 行内数学符号、单变量、字母、式子必须严格用成对的单个美元符 `$ ... $` 包裹。
   - 独立大公式、方程组、多行矩阵（如 array, bmatrix, cases, aligned）必须独立成段，并用成对的双美元符 `$$ ... $$` 包裹。
   - 严禁句子中间把行内公式误写为 `$$`；严禁留下未闭合的单 `$` 或双 `$$`。
3. 矩阵与语法修复：
   - 修复 OCR 导致的字符粘连与语法缺失（如 `\\b {{ a }}` 修复为 `\\mathbf{{a}}`）；
   - 确保矩阵的换行 `\\\\` 和列对齐 `&` 语法严密无损。
4. 纯净输出：直接输出排版修复后的正文，严禁包裹任何外层 ```markdown 代码块！"""

        prompt = f"请对以下学术内容执行排版与数学公式精校修复，直接输出正文：\n\n{page_content}"
        return self.translator.call_llm(prompt, sys_prompt)


def format_academic_cards(markdown_text: str, custom_rules: Optional[List[Tuple[List[str], str, str]]] = None) -> str:
    """
    【学术卡片自动识别与样式注入】
    基于中英文学术关键词，为 Markdown 中的定理、定义、算法等逻辑单元赋予语义化 CSS 卡片样式。
    """
    rules = custom_rules or DEFAULT_CARD_RULES
    result = markdown_text

    for keywords, class_name, _ in rules:
        kw_regex = "|".join(re.escape(k) for k in keywords)
        # 匹配以 **关键词 ...** 开头的学术段落
        pattern = rf'(?m)^(\*\*(?:{kw_regex})[\s\d\.\-—A-Za-z]*\*\*:?[\s\S]*?)(?=(?:\n\s*\n\s*\*\*|\n\s*<div class="page-marker"|$))'
        
        def repl(match):
            content = match.group(1).strip()
            if 'academic-card' in content:
                return match.group(0)
            return f'\n\n<div class="academic-card {class_name}">\n\n{content}\n\n</div>\n\n'
        
        result = re.sub(pattern, repl, result)

    return result
