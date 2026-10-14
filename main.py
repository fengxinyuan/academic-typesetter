# -*- coding: utf-8 -*-
"""
统一学术排版与文献翻译工作流 (Academic Typesetter CLI)
支持处理任意论文、专著、技术报告，全面消除硬编码，提供模块化端到端管道。
"""

import os
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import argparse
import shutil

from core.config import (
    find_browser_executable, detect_chinese_font, get_default_model,
    DEFAULT_MAX_WORKERS, DEFAULT_OUTPUT_ROOT, WORKSPACE_DIR
)
from core.mineru import MinerUClient, assemble_mineru_markdown
from core.translator import AcademicTranslator
from core.typesetter import PageHealer, format_academic_cards
from core.exporter import export_markdown, export_html, export_bilingual_html, export_bilingual_pdf_html, export_pdf_via_browser


def process_pipeline(input_path: str,
                     task: str = "translate",
                     target_lang: str = "zh-CN",
                     domain: str = "academic",
                     model_name: str = None,
                     max_workers: int = DEFAULT_MAX_WORKERS,
                     output_dir: str = None,
                     export_pdf: bool = True):
    """
    通用学术文献处理流水线
    根据输入文件类型 (PDF 或 Markdown) 自动执行提取、翻译、自愈排版与多模态导出。
    """
    input_abs = os.path.abspath(input_path)
    if not os.path.exists(input_abs):
        print(f"[ERROR] 输入文件不存在: {input_abs}")
        sys.exit(1)

    file_stem = os.path.splitext(os.path.basename(input_abs))[0]
    out_dir = os.path.abspath(output_dir or os.path.join(DEFAULT_OUTPUT_ROOT, file_stem))
    os.makedirs(out_dir, exist_ok=True)

    print("=" * 60)
    print(f" 学术文献处理工作流启动")
    print(f" 输入文件: {input_abs}")
    print(f" 执行任务: {task.upper()} | 目标语言: {target_lang} | 领域: {domain}")
    print(f" 输出目录: {out_dir}")
    print("=" * 60)

    # 1. 如果输入是 PDF，先进行 MinerU 结构化提取
    is_pdf = input_abs.lower().endswith(".pdf")
    if is_pdf:
        print("\n【步骤 1】MinerU 学术版面与数学公式结构化提取...")
        mineru_extract_dir = os.path.join(out_dir, "mineru_extracted")
        client = MinerUClient()
        client.extract_pdf(input_abs, mineru_extract_dir)

        print("正在装配结构化 Markdown 与公式指纹映射...")
        en_markdown, eq_img_map = assemble_mineru_markdown(mineru_extract_dir)
        
        # 复制图片目录到输出目录
        src_images = os.path.join(mineru_extract_dir, "images")
        dst_images = os.path.join(out_dir, "images")
        if os.path.exists(src_images) and not os.path.exists(dst_images):
            shutil.copytree(src_images, dst_images)

        # 导出原文 Markdown
        en_md_path = os.path.join(out_dir, f"{file_stem}_ORIGINAL.md")
        export_markdown(en_markdown, en_md_path)
        print(f"[OK] 原文 Markdown 已保存至: {en_md_path}")
    else:
        # 输入直接为 Markdown 源码
        with open(input_abs, "r", encoding="utf-8") as f:
            en_markdown = f.read()
        eq_img_map = {}

    if task == "extract":
        print("\n[SUCCESS] 仅提取任务完成！")
        return

    # 2. 执行翻译或排版
    progress_file = os.path.join(out_dir, "translation_progress.json")
    translator = AcademicTranslator(
        model_name=model_name or get_default_model(),
        target_lang=target_lang,
        domain=domain
    )

    if task in ["translate", "bilingual"]:
        print(f"\n【步骤 2】启动 {max_workers} 线程并发学术翻译 (带公式哨兵保护)...")
        translated_md = translator.translate_document(
            markdown_text=en_markdown,
            progress_cache_path=progress_file,
            max_workers=max_workers
        )
    else:
        # typeset 模式：不翻译，仅做排版美化
        translated_md = en_markdown

    print("\n【步骤 3】注入出版级学术卡片 (定理/定义/例题/证明)...")
    final_md = format_academic_cards(translated_md)

    # 3. 产物导出
    print("\n【步骤 4】导出多模态成果物...")
    out_md_path = os.path.join(out_dir, f"{file_stem}_{target_lang}.md")
    export_markdown(final_md, out_md_path)
    print(f"  📖 纯净 Markdown: {out_md_path}")

    out_html_path = os.path.join(out_dir, f"{file_stem}_{target_lang}.html")
    export_html(final_md, out_html_path, title=file_stem, eq_img_map=eq_img_map)
    print(f"  🌐 交互式 HTML (KaTeX): {out_html_path}")

    if task == "bilingual":
        out_bi_html = os.path.join(out_dir, f"{file_stem}_Bilingual.html")
        export_bilingual_html(en_markdown, final_md, out_bi_html, title=file_stem)
        print(f"  🪟 双语对照阅读器: {out_bi_html}")

        # 出版级双语对照 PDF
        out_bi_print_html = os.path.join(out_dir, f"{file_stem}_Bilingual_print.html")
        export_bilingual_pdf_html(en_markdown, final_md, out_bi_print_html, title=file_stem)
        
        if export_pdf:
            print("\n正在通过无头浏览器生成高保真【中英双语对照矢量 PDF】...")
            out_bi_pdf = os.path.join(out_dir, f"{file_stem}_Bilingual.pdf")
            try:
                export_pdf_via_browser(out_bi_print_html, out_bi_pdf)
                print(f"  📑 出版级双语矢量 PDF: {out_bi_pdf}")
            except Exception as e:
                print(f"  [WARN] 双语 PDF 导出失败: {e}")

    if export_pdf:
        print("\n正在通过无头浏览器生成高保真【纯中文出版级矢量 PDF】...")
        out_pdf_path = os.path.join(out_dir, f"{file_stem}_{target_lang}.pdf")
        try:
            export_pdf_via_browser(out_html_path, out_pdf_path)
            print(f"  📑 出版级中文矢量 PDF: {out_pdf_path}")
        except Exception as e:
            print(f"  [WARN] 中文 PDF 导出跳过或出错: {e}")

    print("\n" + "=" * 60)
    print(f"🎉 全部处理完毕！所有成果物已归档至: {out_dir}")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(description="学术文献智能翻译与出版级排版工具 (Academic Typesetter)")
    subparsers = parser.add_subparsers(dest="subcommand", help="子命令")

    # process 子命令
    p_proc = subparsers.add_parser("process", help="端到端处理文档 (提取+翻译+排版+导出)")
    p_proc.add_argument("input", help="输入的 PDF 或 Markdown 文件路径")
    p_proc.add_argument("--task", choices=["translate", "typeset", "bilingual", "extract"], default="translate", help="任务类型")
    p_proc.add_argument("--lang", default="zh-CN", help="目标语言 (默认 zh-CN)")
    p_proc.add_argument("--domain", choices=["academic", "math", "general"], default="academic", help="学术领域")
    p_proc.add_argument("--model", default=None, help="LLM 模型名称 (默认自适应)")
    p_proc.add_argument("--workers", type=int, default=DEFAULT_MAX_WORKERS, help="并发线程数")
    p_proc.add_argument("--outdir", default=None, help="输出目录路径 (默认 ./output/<文件名>/)")
    p_proc.add_argument("--no-pdf", action="store_true", help="跳过生成 PDF")

    # typeset 子命令
    p_type = subparsers.add_parser("typeset", help="仅执行学术排版美化与卡片注入")
    p_type.add_argument("input", help="输入的 Markdown 文件路径")
    p_type.add_argument("--outdir", default=None, help="输出目录")

    # bilingual 子命令
    p_bi = subparsers.add_parser("bilingual", help="生成中英双语分屏对照阅读器")
    p_bi.add_argument("input", help="输入的 PDF 文件路径")
    p_bi.add_argument("--outdir", default=None, help="输出目录")

    # info 子命令
    p_info = subparsers.add_parser("info", help="查看系统环境与已检测到的浏览器/字体/模型")

    # serve 子命令
    p_serve = subparsers.add_parser("serve", help="启动可视化 Web 双语排版工作台")
    p_serve.add_argument("--host", default="127.0.0.1", help="监听地址 (默认 127.0.0.1)")
    p_serve.add_argument("--port", type=int, default=8000, help="监听端口 (默认 8000)")

    args = parser.parse_args()

    if args.subcommand == "info":
        print("=" * 50)
        print(" Academic Typesetter 环境检测报告")
        print("=" * 50)
        print(f"工作区目录:   {WORKSPACE_DIR}")
        print(f"默认模型:     {get_default_model()}")
        print(f"无头浏览器:   {find_browser_executable() or '未检测到 (请安装 Chrome 或 Edge)'}")
        print(f"中文字体:     {detect_chinese_font()}")
        print("=" * 50)
        return

    if args.subcommand == "serve":
        from web.server import start_server
        start_server(host=args.host, port=args.port)
        return

    if args.subcommand in ["process", "typeset", "bilingual"]:
        task = "typeset" if args.subcommand == "typeset" else ("bilingual" if args.subcommand == "bilingual" else getattr(args, "task", "translate"))
        process_pipeline(
            input_path=args.input,
            task=task,
            target_lang=getattr(args, "lang", "zh-CN"),
            domain=getattr(args, "domain", "academic"),
            model_name=getattr(args, "model", None),
            max_workers=getattr(args, "workers", DEFAULT_MAX_WORKERS),
            output_dir=getattr(args, "outdir", None),
            export_pdf=not getattr(args, "no_pdf", False)
        )
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
