# -*- coding: utf-8 -*-
"""
统一配置与环境管理器
杜绝任何硬编码，支持环境变量、操作系统注册表、动态字体探测与自适应模型选择。
"""

import os
import sys
import shutil
from typing import Optional, List

# 工作区根目录
WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 优先加载本地 .env 文件
_env_file = os.path.join(WORKSPACE_DIR, ".env")
if os.path.exists(_env_file):
    with open(_env_file, "r", encoding="utf-8") as _ef:
        for _line in _ef:
            _line = _line.strip()
            if _line and not _line.startswith("#") and "=" in _line:
                _k, _v = _line.split("=", 1)
                os.environ.setdefault(_k.strip(), _v.strip())

# API 密钥配置 (统一从环境读取)
MINERU_TOKEN = os.getenv("MINERU_TOKEN", "").strip()
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY", "").strip()
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "").strip()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "").strip()

# 默认并发线程数与输出根目录
DEFAULT_MAX_WORKERS = int(os.getenv("MAX_WORKERS", "5"))
DEFAULT_OUTPUT_ROOT = os.getenv("OUTPUT_DIR", os.path.join(WORKSPACE_DIR, "output"))

def get_default_model() -> str:
    """根据已配置的 API Key 动态确定最优默认模型，无需用户手动硬编码"""
    explicit = os.getenv("DEFAULT_MODEL", "").strip()
    if explicit:
        return explicit
    if DASHSCOPE_API_KEY:
        return "qwen-plus"
    if DEEPSEEK_API_KEY:
        return "deepseek-chat"
    if OPENAI_API_KEY:
        return "gpt-4o"
    return "qwen-plus"

def find_browser_executable() -> Optional[str]:
    """
    动态探测无头浏览器执行路径：
    1. 优先读取用户在 .env / 环境变量中配置的 BROWSER_PATH 或 CHROME_PATH
    2. PATH 环境变量自动检索 (shutil.which)
    3. Windows 平台：查询系统官方注册表 (winreg App Paths)，彻底杜绝因安装路径不同而失效
    4. Linux / macOS 标准安装目录动态扫描
    """
    # 1. 显式环境变量
    for env_key in ["BROWSER_PATH", "CHROME_PATH", "EDGE_PATH"]:
        custom_path = os.getenv(env_key, "").strip()
        if custom_path and os.path.isfile(custom_path):
            return custom_path

    # 2. PATH 环境变量检索
    search_names = ["chrome", "msedge", "google-chrome", "chromium", "chromium-browser", "brave"]
    if sys.platform == "win32":
        search_names = [f"{n}.exe" for n in search_names]
    for name in search_names:
        found = shutil.which(name)
        if found and os.path.isfile(found):
            return found

    # 3. Windows 平台：通过官方 Windows 注册表 App Paths 定位
    if sys.platform == "win32":
        try:
            import winreg
            app_names = ["chrome.exe", "msedge.exe", "brave.exe"]
            for app in app_names:
                for root in [winreg.HKEY_CURRENT_USER, winreg.HKEY_LOCAL_MACHINE]:
                    sub_key = rf"Software\Microsoft\Windows\CurrentVersion\App Paths\{app}"
                    try:
                        with winreg.OpenKey(root, sub_key) as k:
                            val, _ = winreg.QueryValueEx(k, "")
                            if val and os.path.isfile(val):
                                return val
                    except OSError:
                        pass
        except Exception:
            pass

    # 4. 常见系统安装路径兜底
    candidates = []
    if sys.platform == "win32":
        windir = os.environ.get("WINDIR", r"C:\Windows")
        prog_files = os.environ.get("ProgramFiles", r"C:\Program Files")
        prog_files_x86 = os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)")
        local_app_data = os.environ.get("LOCALAPPDATA", "")
        
        candidates.extend([
            os.path.join(prog_files, "Google", "Chrome", "Application", "chrome.exe"),
            os.path.join(prog_files_x86, "Google", "Chrome", "Application", "chrome.exe"),
            os.path.join(prog_files, "Microsoft", "Edge", "Application", "msedge.exe"),
            os.path.join(prog_files_x86, "Microsoft", "Edge", "Application", "msedge.exe"),
        ])
        if local_app_data:
            candidates.extend([
                os.path.join(local_app_data, "Google", "Chrome", "Application", "chrome.exe"),
                os.path.join(local_app_data, "Microsoft", "Edge", "Application", "msedge.exe"),
            ])
    elif sys.platform == "darwin":
        candidates.extend([
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
            "/Applications/Chromium.app/Contents/MacOS/Chromium",
        ])
    else:  # Linux
        candidates.extend([
            "/usr/bin/google-chrome",
            "/usr/bin/google-chrome-stable",
            "/usr/bin/chromium",
            "/usr/bin/chromium-browser",
            "/snap/bin/chromium",
        ])

    for c in candidates:
        if os.path.isfile(c):
            return c

    return None

def detect_chinese_font() -> str:
    """
    动态检测系统中适用的中文字体路径：
    1. 优先读取 FONT_PATH 环境变量
    2. 动态扫描操作系统字体库目录
    """
    custom = os.getenv("FONT_PATH", "").strip()
    if custom and os.path.isfile(custom):
        return custom

    # 常见 CJK 字体优先级列表
    target_names = [
        "msyh.ttc", "msyhl.ttc", "simsun.ttc", "simhei.ttf", "NotoSansSC-Regular.otf",
        "NotoSansCJK-Regular.ttc", "PingFang.ttc", "SourceHanSansSC-Regular.otf"
    ]

    font_dirs = []
    if sys.platform == "win32":
        windir = os.environ.get("WINDIR", r"C:\Windows")
        font_dirs.append(os.path.join(windir, "Fonts"))
        local_fonts = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Microsoft", "Windows", "Fonts")
        if os.path.isdir(local_fonts):
            font_dirs.append(local_fonts)
    elif sys.platform == "darwin":
        font_dirs.extend(["/System/Library/Fonts", "/Library/Fonts", os.path.expanduser("~/Library/Fonts")])
    else:
        font_dirs.extend(["/usr/share/fonts", "/usr/local/share/fonts", os.path.expanduser("~/.fonts")])

    for d in font_dirs:
        for fname in target_names:
            p = os.path.join(d, fname)
            if os.path.isfile(p):
                return p

    # 兜底返回系统默认
    if font_dirs and os.path.isdir(font_dirs[0]):
        return font_dirs[0]
    return "Arial"
