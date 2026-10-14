# -*- coding: utf-8 -*-
"""
统一出版物导出引擎 · 专业学术版
支持纯净 Markdown、单文件交互式 KaTeX HTML、多模态双语阅读器及无头浏览器出版级矢量 PDF。
全面优化：
1. 采用高密度学术流式排版 (Interleaved & Split Switchable)，彻底解决两栏挤压与大空白顽疾；
2. 紧凑学术版心：大幅精简标题与头部空间，单页容纳 3-4 个完整对齐段落；
3. 杜绝中英文标题括号重复与页码标记泄漏；
4. 出版级学术三线表 (Booktabs) 与 KaTeX 矢量数学公式；
5. 多视图自适应切换：逐段精读 / 左右分屏 / 仅中文 / 仅英文。
"""

import os
import sys
import re
import json
import shutil
import subprocess
from typing import Optional, Dict, List

from core.config import find_browser_executable

# ==============================================================================
# 单文档出版级 HTML 模板 (含 KaTeX、三线表、自适应夜间模式)
# ==============================================================================
HTML_READER_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>__TITLE__</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/marked@4.3.0/marked.min.js"></script>
    <style>
        :root {
            --bg-color: #f8fafc;
            --text-color: #0f172a;
            --card-bg: #ffffff;
            --border-color: #e2e8f0;
            --primary-accent: #2563eb;
            --heading-color: #0f172a;
        }
        [data-theme="dark"] {
            --bg-color: #0f172a;
            --text-color: #e2e8f0;
            --card-bg: #1e293b;
            --border-color: #334155;
            --primary-accent: #60a5fa;
            --heading-color: #f8fafc;
        }
        @page {
            size: A4 portrait;
            margin: 16mm 18mm 16mm 18mm;
        }
        * { box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Noto Sans CJK SC", sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.72;
            margin: 0;
            padding: 0;
            font-size: 10pt;
            transition: background-color 0.3s, color 0.3s;
        }
        .container {
            max-width: 880px;
            margin: 0 auto;
            padding: 36px 44px;
            background: var(--card-bg);
            box-shadow: 0 4px 20px -2px rgba(0,0,0,0.05);
            min-height: 100vh;
        }
        @media print {
            body { background: #fff !important; }
            .container { max-width: 100% !important; margin: 0 !important; padding: 0 !important; box-shadow: none !important; }
            .toolbar { display: none !important; }
            .page-marker { display: none !important; }
            table { page-break-inside: avoid !important; }
            img { page-break-inside: avoid !important; }
            h1, h2, h3 { page-break-after: avoid !important; }
            .academic-card { page-break-inside: avoid !important; }
        }
        h1, h2, h3, h4 {
            color: var(--heading-color);
            font-weight: 700;
            page-break-after: avoid;
        }
        h1 { font-size: 1.45rem; text-align: center; margin: 18px 0 10px; line-height: 1.35; font-weight: 800; }
        h2 { font-size: 1.18rem; margin: 18px 0 8px; border-bottom: 1.2px solid var(--border-color); padding-bottom: 4px; }
        h3 { font-size: 1.02rem; margin: 14px 0 6px; }
        p { margin: 8px 0; text-align: justify; text-justify: inter-ideograph; }

        .toolbar {
            position: fixed;
            top: 18px;
            right: 18px;
            z-index: 1000;
            display: flex;
            gap: 8px;
        }
        .toolbar-btn {
            background: var(--card-bg);
            color: var(--text-color);
            border: 1px solid var(--border-color);
            padding: 6px 12px;
            border-radius: 6px;
            cursor: pointer;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            font-size: 12px;
            font-weight: 500;
        }

        .academic-card {
            border-radius: 0 4px 4px 0;
            padding: 9px 14px;
            margin: 12px 0;
            border-left: 3.5px solid #94a3b8;
            background: rgba(148, 163, 184, 0.05);
            page-break-inside: avoid;
        }
        .card-theorem { border-left-color: #2563eb; background: rgba(37, 99, 235, 0.04); }
        .card-definition { border-left-color: #475569; background: rgba(71, 85, 105, 0.04); }
        .card-lemma { border-left-color: #7c3aed; background: rgba(124, 58, 237, 0.04); }
        .card-algorithm { border-left-color: #0d9488; background: rgba(13, 148, 136, 0.04); }
        .card-example { border-left-color: #16a34a; background: rgba(22, 163, 74, 0.04); }
        .card-exercise { border-left-color: #ea580c; background: rgba(234, 88, 12, 0.04); }
        .card-proof { border-left-color: #cbd5e1; background: transparent; padding-left: 12px; font-style: italic; }
        .card-remark { border-left-color: #d97706; background: rgba(217, 119, 6, 0.04); }

        /* 出版级学术三线表 (Booktabs) */
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 16px 0;
            font-size: 8.8pt;
            line-height: 1.45;
            border-top: 1.8px solid #0f172a;
            border-bottom: 1.8px solid #0f172a;
            page-break-inside: avoid;
            background: #fff;
        }
        th, td { padding: 6px 10px; text-align: center; }
        th { border-bottom: 1px solid #0f172a; background-color: #f8fafc; font-weight: 600; color: #0f172a; }
        td { border-bottom: 1px solid #e2e8f0; }
        tr:last-child td { border-bottom: none; }

        img {
            max-width: 86%;
            height: auto;
            display: block;
            margin: 14px auto;
            border-radius: 4px;
            page-break-inside: avoid;
        }

        .math-block-container {
            margin: 12px 0;
            text-align: center;
            overflow-x: auto;
            max-width: 100%;
        }
        .katex-display { margin: 0 !important; }
        .formula-img { max-width: 100%; height: auto; vertical-align: middle; }
    </style>
</head>
<body>
    <div class="toolbar">
        <button class="toolbar-btn" onclick="toggleTheme()">🌓 主题</button>
        <button class="toolbar-btn" onclick="window.print()">🖨️ 打印 / 导出 PDF</button>
    </div>
    <div class="container" id="content"></div>

    <script id="raw-markdown" type="text/plain">__RAW_MD_PLACEHOLDER__</script>

    <script>
        function toggleTheme() {
            const current = document.documentElement.getAttribute('data-theme');
            document.documentElement.setAttribute('data-theme', current === 'dark' ? 'light' : 'dark');
        }

        document.addEventListener("DOMContentLoaded", function () {
            let rawContent = document.getElementById('raw-markdown').textContent;
            
            // 剥离原稿中的 page-marker 标签，防止泄露
            rawContent = rawContent.replace(/<div class="page-marker"[^>]*>[\\s\\S]*?<\\/div>/g, '');
            rawContent = rawContent.replace(/id="page-\\d+">[\\s\\S]*?<\\/div>/g, '');
            
            const mathTokens = [];
            function saveMath(content, isBlock) {
                const idx = mathTokens.length;
                mathTokens.push({ content: content, isBlock: isBlock });
                return 'KXMATHTOKEN' + idx + 'END';
            }

            rawContent = rawContent.replace(/\\$\\$([\\s\\S]*?)\\$\\$/g, function(match, body) {
                return '\\n\\n' + saveMath(body.trim(), true) + '\\n\\n';
            });
            rawContent = rawContent.replace(/(^|[^\\\\$])\\$([^\\s$\\n\\r\\u4e00-\\u9fa5][^$\\n\\r]*?)\\$(?!\\$)/g, function(match, pre, body) {
                return pre + saveMath(body.trim(), false);
            });

            const EQ_IMG_MAP = __EQ_IMG_MAP_PLACEHOLDER__;
            function fingerprint(latex) {
                if (!latex) return '';
                return latex.replace(/\\s+/g, '').replace(/\\\\left/g, '').replace(/\\\\right/g, '').replace(/[{}]/g, '');
            }

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
                    const fp = fingerprint(token.content);
                    const img = EQ_IMG_MAP[fp];
                    rendered = img ? '<img class="formula-img" src="' + img + '" alt="formula">' : '<code>' + token.content + '</code>';
                }
                if (token.isBlock) {
                    rendered = '<div class="math-block-container">' + rendered + '</div>';
                }
                renderedById[i] = rendered;
            }

            let html = marked.parse(rawContent);
            html = html.replace(/<p>\\s*KXMATHTOKEN(\\d+)END\\s*<\\/p>/g, function(m, n) {
                return renderedById[+n] || m;
            });
            html = html.replace(/KXMATHTOKEN(\\d+)END/g, function(m, n) {
                return renderedById[+n] || m;
            });

            document.getElementById('content').innerHTML = html;
        });
    </script>
</body>
</html>
"""

# ==============================================================================
# 🌟 全新多模态学术双语模板 (支持逐段精读 / 左右分屏 / 仅中文 / 仅英文)
# ==============================================================================
BILINGUAL_UNIFIED_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>__TITLE__ · 学术双语精读阅读器</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/marked@4.3.0/marked.min.js"></script>
    <style>
        :root {
            --bg-page: #f8fafc;
            --bg-card: #ffffff;
            --text-main: #0f172a;
            --text-en: #334155;
            --text-muted: #64748b;
            --primary: #2563eb;
            --border-color: #e2e8f0;
            --zh-card-bg: #f8fafc;
            --zh-card-border: #3b82f6;
        }

        @page {
            size: A4 portrait;
            margin: 16mm 18mm 16mm 18mm;
        }

        * { box-sizing: border-box; }
        body {
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
            background: var(--bg-page);
            color: var(--text-main);
            font-size: 10pt;
            line-height: 1.7;
        }

        /* 顶部紧凑控制栏 (屏幕展示，打印隐藏) */
        .top-navbar {
            background: #0f172a;
            color: #fff;
            padding: 10px 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0,0,0,0.12);
        }
        .top-navbar .brand {
            font-size: 14px;
            font-weight: 600;
            letter-spacing: 0.5px;
        }
        .nav-controls {
            display: flex;
            gap: 8px;
        }
        .mode-btn {
            background: #1e293b;
            color: #cbd5e1;
            border: 1px solid #334155;
            padding: 5px 12px;
            border-radius: 6px;
            font-size: 12px;
            cursor: pointer;
            transition: all 0.15s ease;
        }
        .mode-btn:hover { background: #334155; color: #fff; }
        .mode-btn.active { background: var(--primary); color: #fff; border-color: var(--primary); font-weight: 600; }

        .article-container {
            max-width: 880px;
            margin: 20px auto;
            background: var(--bg-card);
            padding: 36px 44px;
            border-radius: 8px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.04);
            min-height: 100vh;
        }

        @media print {
            body { background: #fff !important; }
            .top-navbar { display: none !important; }
            .article-container {
                max-width: 100% !important;
                margin: 0 !important;
                padding: 0 !important;
                box-shadow: none !important;
                border-radius: 0 !important;
            }
            .bilingual-pair { page-break-inside: avoid !important; }
            .academic-card { page-break-inside: avoid !important; }
            table { page-break-inside: avoid !important; }
            img { page-break-inside: avoid !important; }
            h1, h2, h3 { page-break-after: avoid !important; }
        }

        /* 🌟 极致紧凑高雅的学术论文头部 */
        .paper-header {
            text-align: center;
            margin-bottom: 20px;
            padding-bottom: 14px;
            border-bottom: 1.5px solid #0f172a;
        }
        .paper-title-zh {
            font-size: 1.45rem;
            font-weight: 800;
            color: #0f172a;
            margin: 0 0 6px 0;
            line-height: 1.35;
        }
        .paper-title-en {
            font-size: 1.05rem;
            font-weight: 600;
            color: #475569;
            margin: 0 0 8px 0;
            font-family: Georgia, 'Times New Roman', serif;
        }
        .paper-authors {
            font-size: 8.8pt;
            color: var(--text-muted);
            margin-top: 6px;
        }

        /* 紧凑章节标题 */
        h2 {
            font-size: 1.18rem;
            font-weight: 700;
            color: #0f172a;
            margin: 20px 0 8px;
            border-bottom: 1.2px solid #e2e8f0;
            padding-bottom: 4px;
        }
        h2 .sub-heading-en {
            font-size: 0.92rem;
            font-weight: normal;
            color: #64748b;
            font-family: Georgia, 'Times New Roman', serif;
            margin-left: 6px;
        }
        h3 {
            font-size: 1.02rem;
            font-weight: 600;
            margin: 14px 0 6px;
            color: #1e293b;
        }
        h3 .sub-heading-en {
            font-size: 0.85rem;
            color: #64748b;
            font-weight: normal;
            margin-left: 6px;
        }

        /* 🌟 核心：双语对齐通用容器 (可通过父级类名纯 CSS 无损切换模式) */
        .bilingual-pair {
            margin: 9px 0;
        }
        .para-en {
            color: var(--text-en);
            font-size: 9.8pt;
            line-height: 1.68;
            text-align: justify;
            hyphens: auto;
        }
        .para-zh {
            color: var(--text-main);
            font-size: 10pt;
            line-height: 1.72;
            text-align: justify;
            text-justify: inter-ideograph;
        }

        /* 模式 1：逐段精读 (默认) */
        .view-interleaved .bilingual-pair {
            display: block;
        }
        .view-interleaved .para-en {
            margin-bottom: 4px;
        }
        .view-interleaved .para-zh {
            background: var(--zh-card-bg);
            border-left: 3.5px solid var(--zh-card-border);
            padding: 7px 14px;
            border-radius: 0 4px 4px 0;
        }

        /* 模式 2：左右分栏 (Split View) */
        .view-split {
            max-width: 1400px !important;
        }
        .view-split .bilingual-pair {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 24px;
            align-items: start;
            padding: 8px 12px;
            border-bottom: 1px solid #f1f5f9;
            border-radius: 4px;
        }
        .view-split .bilingual-pair:hover {
            background: rgba(37,99,235,0.035);
        }
        .view-split .para-en {
            border-right: 1px solid var(--border-color);
            padding-right: 18px;
            margin-bottom: 0;
        }
        .view-split .para-zh {
            background: transparent;
            border-left: none;
            padding: 0;
        }

        /* 模式 3：仅中文 (Chinese Only) */
        .view-zh .bilingual-pair { display: block; margin: 10px 0; }
        .view-zh .para-en { display: none; }
        .view-zh .para-zh { background: transparent; border-left: none; padding: 0; }
        .view-zh h2 .sub-heading-en, .view-zh h3 .sub-heading-en, .view-zh .paper-title-en { display: none; }

        /* 模式 4：仅英文 (English Only) */
        .view-en .bilingual-pair { display: block; margin: 10px 0; }
        .view-en .para-zh { display: none; }
        .view-en .para-en { margin-bottom: 0; }
        .view-en .paper-title-zh { display: none; }

        /* 出版级学术三线表 */
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 16px 0;
            font-size: 8.8pt;
            line-height: 1.45;
            border-top: 1.8px solid #0f172a;
            border-bottom: 1.8px solid #0f172a;
            background: #fff;
        }
        th, td { padding: 6px 10px; text-align: center; }
        th { border-bottom: 1px solid #0f172a; background: #f8fafc; font-weight: 600; }
        td { border-bottom: 1px solid #e2e8f0; }
        tr:last-child td { border-bottom: none; }

        /* 学术卡片 */
        .academic-card {
            border-left: 3.5px solid #2563eb;
            background: rgba(37,99,235,0.035);
            padding: 9px 14px;
            margin: 12px 0;
            border-radius: 0 4px 4px 0;
        }

        /* 图片与公式 */
        img {
            max-width: 86%;
            height: auto;
            display: block;
            margin: 14px auto;
            border-radius: 4px;
        }
        .math-block-container {
            margin: 12px 0;
            text-align: center;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <div class="top-navbar">
        <div class="brand">📖 __BRAND_TITLE__</div>
        <div class="nav-controls">
            <button class="mode-btn active" id="btnInterleaved" onclick="switchView('interleaved')">📜 逐段精读</button>
            <button class="mode-btn" id="btnSplit" onclick="switchView('split')">🪟 左右分屏</button>
            <button class="mode-btn" id="btnZh" onclick="switchView('zh')">🇨🇳 仅中文</button>
            <button class="mode-btn" id="btnEn" onclick="switchView('en')">🇺🇸 仅英文</button>
            <button class="mode-btn" onclick="window.print()">🖨️ 导出 PDF</button>
        </div>
    </div>

    <div class="article-container view-interleaved" id="docContainer">
        <!-- 动态装配的学术双语内容 -->
    </div>

    <script id="aligned-raw" type="application/json">__ALIGNED_JSON__</script>

    <script>
        function switchView(mode) {
            document.querySelectorAll('.mode-btn').forEach(b => b.classList.remove('active'));
            const container = document.getElementById('docContainer');
            container.className = 'article-container view-' + mode;
            const btnMap = {
                'interleaved': 'btnInterleaved',
                'split': 'btnSplit',
                'zh': 'btnZh',
                'en': 'btnEn'
            };
            if (btnMap[mode]) {
                document.getElementById(btnMap[mode]).classList.add('active');
            }
        }

        function parseAndRenderMath(rawText) {
            if (!rawText) return "";
            const mathTokens = [];
            let content = rawText;
            content = content.replace(/\\$\\$([\\s\\S]*?)\\$\\$/g, (m, b) => {
                mathTokens.push({ content: b.trim(), isBlock: true });
                return '\\n\\nKXMATHTOKEN' + (mathTokens.length - 1) + 'END\\n\\n';
            });
            content = content.replace(/(^|[^\\\\$])\\$([^\\s$\\n\\r\\u4e00-\\u9fa5][^$\\n\\r]*?)\\$(?!\\$)/g, (m, pre, b) => {
                mathTokens.push({ content: b.trim(), isBlock: false });
                return pre + 'KXMATHTOKEN' + (mathTokens.length - 1) + 'END';
            });

            const rendered = mathTokens.map(t => {
                try {
                    let r = katex.renderToString(t.content, { displayMode: t.isBlock, throwOnError: false, strict: false });
                    return t.isBlock ? '<div class="math-block-container">' + r + '</div>' : r;
                } catch(e) { return '<code>' + t.content + '</code>'; }
            });

            let html = marked.parse(content);
            html = html.replace(/<p>\\s*KXMATHTOKEN(\\d+)END\\s*<\\/p>/g, (m, n) => rendered[+n] || m);
            html = html.replace(/KXMATHTOKEN(\\d+)END/g, (m, n) => rendered[+n] || m);
            return html;
        }

        document.addEventListener("DOMContentLoaded", function() {
            const rawData = JSON.parse(document.getElementById('aligned-raw').textContent);
            const container = document.getElementById('docContainer');
            let docHtml = "";

            rawData.forEach(item => {
                if (item.type === "header") {
                    docHtml += `
                        <div class="paper-header">
                            <h1 class="paper-title-zh">${item.title_zh}</h1>
                            <h2 class="paper-title-en">${item.title_en}</h2>
                            <div class="paper-authors">${item.authors}</div>
                        </div>
                    `;
                } else if (item.type === "heading") {
                    const tag = item.level === 3 ? 'h3' : 'h2';
                    const subEn = item.en ? `<span class="sub-heading-en">(${item.en})</span>` : '';
                    docHtml += `<${tag}>${item.zh} ${subEn}</${tag}>`;
                } else if (item.type === "raw_html") {
                    docHtml += item.content;
                } else if (item.type === "raw_md") {
                    docHtml += parseAndRenderMath(item.content);
                } else if (item.type === "pair") {
                    const enHtml = parseAndRenderMath(item.en);
                    const zhHtml = parseAndRenderMath(item.zh);
                    docHtml += `
                        <div class="bilingual-pair">
                            <div class="para-en">${enHtml}</div>
                            <div class="para-zh">${zhHtml}</div>
                        </div>
                    `;
                }
            });

            container.innerHTML = docHtml;
        });
    </script>
</body>
</html>
"""


def _strip_page_markers(text: str) -> str:
    """彻底剥离任何页码 marker 标签，杜绝泄露"""
    text = re.sub(r'<div class="page-marker"[^>]*>[\s\S]*?</div>', '', text)
    text = re.sub(r'id="page-\d+">.*?</div>', '', text)
    text = re.sub(r'id="page-\d+">[^<]*', '', text)
    return text.strip()


def build_aligned_bilingual_data(en_text: str, zh_text: str) -> List[Dict]:
    """
    【高精度中英文学术对齐构建器】
    提取紧凑论文头部、章节标题（杜绝括号重复）、表格、图片与中英文段落对。
    """
    en_chunks = en_text.split('<div class="page-marker"')
    zh_chunks = zh_text.split('<div class="page-marker"')

    # 1. 第一页尝试提取紧凑标题与作者
    p1_en = _strip_page_markers(en_chunks[1]) if len(en_chunks) > 1 else _strip_page_markers(en_chunks[0])
    p1_zh = _strip_page_markers(zh_chunks[1]) if len(zh_chunks) > 1 else _strip_page_markers(zh_chunks[0])

    en_p1_paras = [x.strip() for x in p1_en.split('\n\n') if x.strip()]
    zh_p1_paras = [x.strip() for x in p1_zh.split('\n\n') if x.strip()]

    title_en = ""
    title_zh = ""
    authors = []

    for p in en_p1_paras:
        if p.startswith('# ') and not title_en:
            title_en = p.lstrip('# ').strip()
        elif not title_en.startswith('#') and not p.startswith('##') and len(authors) < 2 and not p.startswith('{'):
            authors.append(p)

    for p in zh_p1_paras:
        if p.startswith('# ') and not title_zh:
            title_zh = p.lstrip('# ').strip()

    author_line = " · ".join([a.replace('\n', ' ') for a in authors if a])

    aligned_items = []

    # 注入紧凑头部
    if title_zh or title_en:
        aligned_items.append({
            "type": "header",
            "title_zh": title_zh or title_en,
            "title_en": title_en,
            "authors": author_line
        })

    total_pages = max(len(en_chunks), len(zh_chunks))

    for p in range(1, total_pages):
        en_c = _strip_page_markers(en_chunks[p]) if p < len(en_chunks) else ""
        zh_c = _strip_page_markers(zh_chunks[p]) if p < len(zh_chunks) else ""

        en_paras = [x.strip() for x in en_c.split('\n\n') if x.strip()]
        zh_paras = [x.strip() for x in zh_c.split('\n\n') if x.strip()]

        start_idx = 0
        if p == 1 and (title_zh or title_en):
            # 第一页跳过头部已提取的标题与作者
            while start_idx < len(en_paras) and not en_paras[start_idx].startswith('##'):
                start_idx += 1

        max_len = max(len(en_paras), len(zh_paras))
        for i in range(start_idx, max_len):
            en_p = en_paras[i] if i < len(en_paras) else ""
            zh_p = zh_paras[i] if i < len(zh_paras) else ""

            if not en_p and not zh_p:
                continue

            # 标题处理
            if en_p.startswith('#') or zh_p.startswith('#'):
                clean_en_h = re.sub(r'^#+\s*', '', en_p).strip()
                clean_zh_h = re.sub(r'^#+\s*', '', zh_p).strip()
                # 剔除中文标题末尾残留的英文括号（含半角与全角），杜绝显示重复
                clean_zh_h = re.sub(r'\s*[（\(][^）\)]*[A-Za-z][^）\)]*[）\)]\s*$', '', clean_zh_h).strip()
                # 剔除英文标题前缀数字，使结构更优雅
                clean_en_h = re.sub(r'^[\d\.]+\s*', '', clean_en_h).strip()

                level = max(en_p.count('#'), zh_p.count('#'), 2)
                aligned_items.append({
                    "type": "heading",
                    "level": level,
                    "zh": clean_zh_h or clean_en_h,
                    "en": clean_en_h if clean_en_h != clean_zh_h else ""
                })
            elif en_p.startswith('<table>') or zh_p.startswith('<table>'):
                tbl = zh_p if '<table>' in zh_p else en_p
                aligned_items.append({"type": "raw_html", "content": tbl})
            elif en_p.startswith('!['):
                aligned_items.append({"type": "raw_md", "content": en_p})
            elif en_p.startswith('$$') or zh_p.startswith('$$'):
                math_c = en_p if en_p.startswith('$$') else zh_p
                aligned_items.append({"type": "raw_md", "content": math_c})
            else:
                aligned_items.append({
                    "type": "pair",
                    "en": en_p,
                    "zh": zh_p
                })

    return aligned_items


def export_markdown(markdown_text: str, output_path: str):
    """导出纯净 Markdown 文本"""
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown_text)


def export_html(markdown_text: str, output_path: str, title: str = "Academic Document", eq_img_map: Optional[Dict[str, str]] = None):
    """导出自包含 KaTeX 与学术三线表的单语紧凑响应式 HTML"""
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    mapping_json = json.dumps(eq_img_map or {}, ensure_ascii=False).replace('</', '<\\/')
    
    html = HTML_READER_TEMPLATE.replace('__TITLE__', title)
    html = html.replace('__RAW_MD_PLACEHOLDER__', markdown_text)
    html = html.replace('__EQ_IMG_MAP_PLACEHOLDER__', mapping_json)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)


def export_bilingual_html(en_markdown: str, zh_markdown: str, output_path: str, title: str = "Bilingual Reader"):
    """
    导出全新多模态学术双语精读阅读器 HTML
    （支持纯 CSS 无损切换：逐段精读 / 左右分屏 / 仅中文 / 仅英文）
    """
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    aligned_data = build_aligned_bilingual_data(en_markdown, zh_markdown)
    data_json = json.dumps(aligned_data, ensure_ascii=False).replace('</', '<\\/')
    
    html = BILINGUAL_UNIFIED_TEMPLATE.replace('__TITLE__', title)
    html = html.replace('__BRAND_TITLE__', title)
    html = html.replace('__ALIGNED_JSON__', data_json)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)


def export_bilingual_pdf_html(en_markdown: str, zh_markdown: str, output_path: str, title: str = "Bilingual Edition"):
    """导出用于 A4 纵向打印的高密度学术精读 HTML"""
    export_bilingual_html(en_markdown, zh_markdown, output_path, title=title)


def export_pdf_via_browser(html_path: str, output_pdf_path: str, browser_path: Optional[str] = None):
    """
    通过无头 Chrome/Edge 打印高质量矢量 PDF，零公式乱码。
    配置 --virtual-time-budget=8000 保证 KaTeX 完整渲染。
    """
    os.makedirs(os.path.dirname(os.path.abspath(output_pdf_path)), exist_ok=True)
    browser = browser_path or find_browser_executable()
    if not browser:
        raise RuntimeError("未在系统中探测到 Chrome/Edge 浏览器，无法执行矢量 PDF 导出！")

    html_abs = os.path.abspath(html_path)
    output_pdf_abs = os.path.abspath(output_pdf_path)

    cmd = [
        browser,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--allow-file-access-from-files",
        "--enable-local-file-accesses",
        "--no-pdf-header-footer",
        "--virtual-time-budget=8000",
        f"--print-to-pdf={output_pdf_abs}",
        html_abs
    ]

    subprocess.run(cmd, check=True, timeout=120)
