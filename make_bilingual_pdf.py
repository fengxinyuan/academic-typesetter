# -*- coding: utf-8 -*-
"""
生成"原书布局中英对照 PDF"（彻底规避公式乱码）。

核心思想（经多轮验证后的最终方案）：
  - 左页 = 原书扫描页原图（100% 原貌，零处理，公式/图表天然无损）。
  - 右页 = 该页中文译文：正文用中文字体流式排版；
           公式【一律使用 MinerU 从原书切出的公式原图】贴回，绝不重新渲染 LaTeX，
           从根本上杜绝任何公式乱码。
  - 按原书页码锚点 (page-marker) 将译文切分并对齐到每一物理页。

复用已有成果：原始扫描 PDF + MinerU 公式原图 (final_output/images) + 已翻译的中文译文
            (full_translation_progress.json)。全程离线、不调用任何在线服务。

用法:
  python make_bilingual_pdf.py                # 全书
  python make_bilingual_pdf.py 50 69          # 仅物理页 50-69（小样）
"""
import os
import re
import sys
import json
import glob

import pymupdf

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

WS = 'C:/Users/fengxy/Desktop/matrix_translator'
ORIGINAL_PDF = r'C:/Users/fengxy/Downloads/00.Theory of Matrices (2ed. AP 1985).pdf'
EXTRACT = WS + '/extracted_parts'
OUT_DIR = WS + '/final_output'
IMAGES_DIR = OUT_DIR + '/images'
PROGRESS = OUT_DIR + '/full_translation_progress.json'
OUT_PDF = OUT_DIR + '/Theory_of_Matrices_Bilingual.pdf'

CN_FONT = 'C:/Windows/Fonts/msyh.ttc'       # 微软雅黑，正文


# —— 行内公式 LaTeX → 可读 Unicode 文本 转换 ——
# 行内公式结构简单（下标/上标/希腊字母/关系符），转成 Unicode 后用中文字体即可清晰显示，
# 彻底避免暴露 \begin{array}、\operatorname 等 LaTeX 源码（之前右页乱码的根源）。
_GREEK = {
    r'\alpha': 'α', r'\beta': 'β', r'\gamma': 'γ', r'\delta': 'δ', r'\epsilon': 'ε',
    r'\varepsilon': 'ε', r'\zeta': 'ζ', r'\eta': 'η', r'\theta': 'θ', r'\vartheta': 'ϑ',
    r'\iota': 'ι', r'\kappa': 'κ', r'\lambda': 'λ', r'\mu': 'μ', r'\nu': 'ν', r'\xi': 'ξ',
    r'\pi': 'π', r'\rho': 'ρ', r'\sigma': 'σ', r'\tau': 'τ', r'\upsilon': 'υ', r'\phi': 'φ',
    r'\varphi': 'φ', r'\chi': 'χ', r'\psi': 'ψ', r'\omega': 'ω',
    r'\Gamma': 'Γ', r'\Delta': 'Δ', r'\Theta': 'Θ', r'\Lambda': 'Λ', r'\Xi': 'Ξ', r'\Pi': 'Π',
    r'\Sigma': 'Σ', r'\Phi': 'Φ', r'\Psi': 'Ψ', r'\Omega': 'Ω',
}
_OPS = {
    # 仅使用微软雅黑确实含有的符号；缺字的（⋯ ℝ ℂ … 等）改用安全等价写法
    r'\times': '×', r'\cdot': '·', r'\cdots': '...', r'\ldots': '...', r'\dots': '...',
    r'\dotsc': '...', r'\leq': '≤', r'\geq': '≥', r'\neq': '≠', r'\le': '≤', r'\ge': '≥',
    r'\in': '∈', r'\notin': '∉', r'\subset': '⊂', r'\subseteq': '⊆', r'\supset': '⊃',
    r'\cup': '∪', r'\cap': '∩', r'\oplus': '⊕', r'\otimes': '⊗', r'\pm': '±', r'\mp': '∓',
    r'\infty': '∞', r'\partial': '∂', r'\nabla': '∇', r'\forall': '∀', r'\exists': '∃',
    r'\rightarrow': '→', r'\to': '→', r'\leftarrow': '←', r'\Rightarrow': '⇒',
    r'\Leftrightarrow': '⇔', r'\mapsto': '→', r'\approx': '≈', r'\equiv': '≡', r'\sim': '~',
    r'\triangleq': '≜', r'\sum': 'Σ', r'\prod': 'Π', r'\int': '∫', r'\sqrt': '√',
    r'\langle': '〈', r'\rangle': '〉', r'\cong': '≅', r'\perp': '⊥', r'\circ': '∘',
    r'\prime': "'", r'\star': '*', r'\ast': '*', r'\bullet': '·', r'\square': '',
    r'\mathbb{R}': 'R', r'\mathbb{C}': 'C', r'\mathbb{Z}': 'Z', r'\mathbb{N}': 'N', r'\mathbb{Q}': 'Q',
    r'\quad': '  ', r'\qquad': '    ', r'\,': ' ', r'\;': ' ', r'\!': '', r'\ ': ' ',
}
# 微软雅黑缺大量 Unicode 上/下标与数学符号字形（经 fontTools 实测：₀₁₂、⁰⁴、ℝ、ℂ、⋯ 等均缺失，
# 会在 PDF 里显示成空白/豆腐块）。因此一律【不使用】Unicode 上下标，统一回退 ASCII _x / ^x，
# 所有字体都含这些字符，绝对不缺字——以"绝不乱码"为第一优先。
_SUB = {}
_SUP = {}


def latex_inline_to_text(s):
    """把一段行内 LaTeX 转成可读的 Unicode 文本（尽力而为，绝不残留裸命令）。"""
    # 去掉 \operatorname{...} / \operatorname*{...} / \mathrm{...} 等包装，保留内部
    s = re.sub(r'\\operatorname\*?\s*\{([^{}]*)\}', lambda m: m.group(1).replace(' ', ''), s)
    s = re.sub(r'\\mathrm\s*\{([^{}]*)\}', lambda m: m.group(1), s)
    s = re.sub(r'\\(mathbf|boldsymbol|pmb|mathcal|mathfrak|mathbb|text|mathit|mathsf|tilde|bar|hat|vec|widetilde|widehat|dot)\s*\{([^{}]*)\}', r'\2', s)
    # 矩阵/数组环境：去掉环境包装；\begin{array}{rl} 的列规格要连同其后的 {rl} 一起删
    s = re.sub(r'\\begin\{array\}\s*\{[^{}]*\}', '', s)   # 连列规格一起删
    s = re.sub(r'\\begin\{[^}]*\}', '', s)
    s = re.sub(r'\\end\{[^}]*\}', '', s)
    s = s.replace('\\\\', ' ').replace('&', ' ')
    s = s.replace('\\left', '').replace('\\right', '')
    s = re.sub(r'\\tag\s*\{[^}]*\}', '', s)
    s = s.replace('\\tag', '')
    # 希腊字母与运算符
    for k, v in list(_GREEK.items()) + list(_OPS.items()):
        s = s.replace(k, v)
    # 上下标：_ { ... } / ^ { ... } ，以及单字符 _x / ^x
    # 上下标：整组若全部能映射为 Unicode 下/上标就用 Unicode，否则回退为纯 ASCII
    # 的 _内容 / ^内容（去花括号、去空格），绝不产生字体缺字的豆腐块(□)。
    def sub_repl(m):
        inner = re.sub(r'\s+', '', m.group(1))
        if inner and all(c in _SUB for c in inner):
            return ''.join(_SUB[c] for c in inner)
        return '_' + inner if len(inner) <= 1 else '_(' + inner + ')'
    def sup_repl(m):
        inner = re.sub(r'\s+', '', m.group(1))
        if inner and all(c in _SUP for c in inner):
            return ''.join(_SUP[c] for c in inner)
        return '^' + inner if len(inner) <= 1 else '^(' + inner + ')'
    s = re.sub(r'_\s*\{([^{}]*)\}', sub_repl, s)
    s = re.sub(r'\^\s*\{([^{}]*)\}', sup_repl, s)
    s = re.sub(r'_\s*([0-9A-Za-z])', lambda m: _SUB.get(m.group(1), '_' + m.group(1)), s)
    s = re.sub(r'\^\s*([0-9A-Za-z])', lambda m: _SUP.get(m.group(1), '^' + m.group(1)), s)
    # 清理残留花括号与多余空白、未知反斜杠命令
    s = re.sub(r'\\[a-zA-Z]+', '', s)   # 去掉未覆盖的裸命令
    s = s.replace('{', '').replace('}', '')
    # 清理 OCR 残渣：孤立的 "o r"（or 被误拆）、多余的分号/逗号堆叠
    s = re.sub(r'\bo\s+r\b', 'or', s)
    s = re.sub(r'[,;]\s*[,;]+', ',', s)
    s = re.sub(r'\s+', ' ', s).strip()
    s = s.strip(' ,;')
    return s
CHUNK_SIZE = 150                            # 与 run_pipeline 分卷一致

# —— 版面参数 ——
PAGE_W, PAGE_H = 595.0, 842.0               # A4 纵向 (pt)
MARGIN = 42.0
CONTENT_W = PAGE_W - 2 * MARGIN
FONT_SIZE = 10.5
LINE_H = FONT_SIZE * 1.6
HEAD_SIZES = {1: 17, 2: 15, 3: 13, 4: 12, 5: 11.5}


def build_page_marker_map():
    """返回 [(页标, 该页译文文本)]，按原书阅读顺序。"""
    with open(PROGRESS, 'r', encoding='utf-8') as f:
        d = json.load(f)
    full_cn = "\n\n".join(d[str(i)] for i in range(len(d)))
    # 以 page-marker 为分隔切成逐页
    pattern = re.compile(r'<div class="page-marker" id="page-([^"]+)">.*?</div>', re.S)
    segments = []
    last_end = 0
    last_label = None
    for m in pattern.finditer(full_cn):
        if last_label is not None:
            segments.append((last_label, full_cn[last_end:m.start()]))
        last_label = m.group(1)
        last_end = m.end()
    if last_label is not None:
        segments.append((last_label, full_cn[last_end:]))
    return segments


def load_equation_images_by_page():
    """返回 {page_idx(全局物理页,0基): [公式图绝对路径按出现顺序]} 以及块级结构。
    通过 content_list 把每页的 equation / image 块原图按顺序取出。"""
    page_to_imgs = {}
    parts = sorted(glob.glob(os.path.join(EXTRACT, 'part_*')),
                   key=lambda p: int(re.search(r'part_(\d+)', p).group(1)))
    for part_dir in parts:
        pidx = int(re.search(r'part_(\d+)', part_dir).group(1))
        part_start_physical = (pidx - 1) * CHUNK_SIZE  # 0 基物理页起点
        cls = glob.glob(os.path.join(part_dir, '*content_list.json'))
        if not cls:
            continue
        data = json.load(open(cls[0], encoding='utf-8'))
        for b in data:
            if b.get('type') in ('equation', 'image') and b.get('img_path'):
                gp = part_start_physical + int(b.get('page_idx', 0))
                fname = os.path.basename(b['img_path'])
                fpath = os.path.join(IMAGES_DIR, fname)
                if os.path.exists(fpath):
                    page_to_imgs.setdefault(gp, []).append(fpath)
    return page_to_imgs


def label_to_physical_index(label, order_hint):
    """把页标映射到 0 基物理页号。PDF-N -> N-1；其余（罗马/阿拉伯印刷页）用顺序提示。"""
    m = re.match(r'PDF-(\d+)$', label)
    if m:
        return int(m.group(1)) - 1
    return order_hint  # 对印刷页标，用它在序列中的顺序近似对齐


# —— 右页译文渲染（流式）——
def render_translation_page(doc, seg_text, eq_images):
    """新建一页，流式排版译文。公式/图片引用处贴原图；返回继续页数。"""
    page = doc.new_page(width=PAGE_W, height=PAGE_H)
    y = MARGIN
    eq_idx = 0

    def ensure_space(h):
        nonlocal page, y
        if y + h > PAGE_H - MARGIN:
            page = doc.new_page(width=PAGE_W, height=PAGE_H)
            y = MARGIN

    # 规范化：去掉 HTML 页标 div（已用于切分），按行处理
    text = re.sub(r'<div class="page-marker".*?</div>', '', seg_text, flags=re.S)

    # 先把块级公式 $$...$$ 与图片引用 ![](...) 标记成占位，便于顺序贴图
    # 分段：用占位符切出"文本片段"与"公式/图片片段"
    tokens = re.split(r'(\$\$[\s\S]*?\$\$|!\[\]\([^)]*\))', text)

    for tok in tokens:
        tok_stripped = tok.strip()
        if not tok_stripped:
            continue
        is_block_math = tok_stripped.startswith('$$')
        is_img = tok_stripped.startswith('![](')
        if is_block_math or is_img:
            # 贴公式原图（按该页顺序取下一张）
            img_path = None
            if is_img:
                ref = re.search(r'!\[\]\(([^)]*)\)', tok_stripped)
                if ref:
                    cand = os.path.join(IMAGES_DIR, os.path.basename(ref.group(1)))
                    if os.path.exists(cand):
                        img_path = cand
            if img_path is None and eq_idx < len(eq_images):
                img_path = eq_images[eq_idx]
                eq_idx += 1
            if img_path and os.path.exists(img_path):
                try:
                    pix = pymupdf.Pixmap(img_path)
                    iw, ih = pix.width, pix.height
                    disp_w = min(CONTENT_W, iw * 0.75)   # 适度缩放
                    disp_h = disp_w * ih / iw
                    if disp_h > PAGE_H - 2 * MARGIN:
                        disp_h = PAGE_H - 2 * MARGIN
                        disp_w = disp_h * iw / ih
                    ensure_space(disp_h + 8)
                    x0 = MARGIN + (CONTENT_W - disp_w) / 2
                    page.insert_image(pymupdf.Rect(x0, y, x0 + disp_w, y + disp_h), filename=img_path)
                    y += disp_h + 10
                except Exception:
                    pass
            continue

        # 普通文本：按段落/标题流式排版
        for para in re.split(r'\n{2,}', tok):
            para = para.strip()
            if not para:
                continue
            # 行内公式 $...$ 在译文里保留为文本（多为简单符号，中文字体可显示大部分）
            # 标题
            hmatch = re.match(r'^(#{1,5})\s+(.*)$', para)
            size = FONT_SIZE
            if hmatch:
                level = len(hmatch.group(1))
                para = hmatch.group(2)
                size = HEAD_SIZES.get(level, FONT_SIZE)
            # 去掉 markdown 粗体标记
            para = para.replace('**', '')
            # 行内公式 $...$ → 可读 Unicode 文本（不暴露 LaTeX 源码）
            para = re.sub(r'\$([^$]+?)\$', lambda m: latex_inline_to_text(m.group(1)), para)
            # 清理任何残留的单个 $
            para = para.replace('$', '')
            lh = size * 1.6
            ensure_space(lh)
            rect = pymupdf.Rect(MARGIN, y, PAGE_W - MARGIN, PAGE_H - MARGIN)
            rc = page.insert_textbox(
                rect, para, fontsize=size, fontname='msyh', fontfile=CN_FONT,
                lineheight=1.6, align=0,
            )
            # insert_textbox 返回剩余高度(负=溢出)；用其估算实际占用并换页续排
            # 简化：按文本长度估行数推进 y
            import math
            approx_chars_per_line = max(1, int(CONTENT_W / (size * 0.95)))
            lines = max(1, math.ceil(len(para) / approx_chars_per_line))
            used = lines * lh + 4
            if rc < 0:  # 溢出，换页续写剩余（粗略处理：换页重排该段）
                page = doc.new_page(width=PAGE_W, height=PAGE_H)
                y = MARGIN
                page.insert_textbox(
                    pymupdf.Rect(MARGIN, y, PAGE_W - MARGIN, PAGE_H - MARGIN),
                    para, fontsize=size, fontname='msyh', fontfile=CN_FONT,
                    lineheight=1.6, align=0,
                )
                y += used
            else:
                y += used


def main():
    args = sys.argv[1:]
    page_from = int(args[0]) if len(args) >= 1 else 1
    page_to = int(args[1]) if len(args) >= 2 else None

    src = pymupdf.open(ORIGINAL_PDF)
    total = len(src)
    if page_to is None:
        page_to = total
    page_to = min(page_to, total)

    segments = build_page_marker_map()
    eq_by_page = load_equation_images_by_page()

    # 建立 物理页(0基) -> 译文片段 的映射
    phys_to_seg = {}
    for order_hint, (label, seg) in enumerate(segments):
        pi = label_to_physical_index(label, order_hint)
        phys_to_seg[pi] = seg

    out = pymupdf.open()
    print(f"生成对照 PDF: 物理页 {page_from}..{page_to}")
    for phys in range(page_from - 1, page_to):
        # —— 左页：原书扫描页原图 ——
        left = out.new_page(width=PAGE_W, height=PAGE_H)
        left.show_pdf_page(pymupdf.Rect(0, 0, PAGE_W, PAGE_H), src, phys)
        # 页脚标注
        left.insert_textbox(pymupdf.Rect(0, PAGE_H - 24, PAGE_W, PAGE_H - 8),
                            f"原书 第 {phys+1} 物理页 (原文)", fontsize=8,
                            fontname='msyh', fontfile=CN_FONT, align=1, color=(0.4, 0.4, 0.4))
        # —— 右页：中文译文 ——
        seg = phys_to_seg.get(phys, "")
        if not seg.strip():
            p = out.new_page(width=PAGE_W, height=PAGE_H)
            p.insert_textbox(pymupdf.Rect(MARGIN, PAGE_H/2, PAGE_W-MARGIN, PAGE_H/2+40),
                             "（本页为扉页/图版，无正文译文）", fontsize=11,
                             fontname='msyh', fontfile=CN_FONT, align=1, color=(0.5,0.5,0.5))
        else:
            render_translation_page(out, seg, eq_by_page.get(phys, []))
        if (phys + 1) % 20 == 0:
            print(f"  已处理到物理页 {phys+1}")

    out.save(OUT_PDF, deflate=True, garbage=4)
    out.close()
    src.close()
    print(f"[SUCCESS] 对照 PDF 已生成: {OUT_PDF}")


if __name__ == '__main__':
    main()
