# -*- coding: utf-8 -*-
"""
学术排版与文献翻译 Web Studio 服务的后端引擎
基于 FastAPI 构建，提供拖拽上传、进度通知、双语实时对照与成果物一键下载。
"""

import os
import sys
import shutil
import threading
from typing import Optional
from fastapi import FastAPI, UploadFile, File, Form, BackgroundTasks
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from core.config import (
    WORKSPACE_DIR, DEFAULT_OUTPUT_ROOT, get_default_model,
    find_browser_executable, detect_chinese_font
)
from main import process_pipeline

app = FastAPI(title="Academic Typesetter Studio")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

WEB_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(WORKSPACE_DIR, "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(DEFAULT_OUTPUT_ROOT, exist_ok=True)

# 挂载静态文件
STATIC_DIR = os.path.join(WEB_DIR, "static")
os.makedirs(STATIC_DIR, exist_ok=True)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# 任务状态跟踪
TASK_STATUS = {}


@app.get("/", response_class=HTMLResponse)
async def serve_index():
    index_file = os.path.join(WEB_DIR, "index.html")
    with open(index_file, "r", encoding="utf-8") as f:
        return f.read()


@app.get("/api/info")
async def get_system_info():
    return {
        "workspace": WORKSPACE_DIR,
        "default_model": get_default_model(),
        "browser": find_browser_executable(),
        "font": detect_chinese_font(),
    }


def run_pipeline_thread(doc_id: str, file_path: str, task: str, target_lang: str, domain: str, model_name: Optional[str]):
    try:
        TASK_STATUS[doc_id] = {"status": "processing", "progress": "正在启动流水线...", "error": None}
        
        file_stem = os.path.splitext(os.path.basename(file_path))[0]
        out_dir = os.path.join(DEFAULT_OUTPUT_ROOT, file_stem)
        
        process_pipeline(
            input_path=file_path,
            task=task,
            target_lang=target_lang,
            domain=domain,
            model_name=model_name,
            output_dir=out_dir,
            export_pdf=True
        )

        TASK_STATUS[doc_id] = {
            "status": "completed",
            "progress": "处理完成！",
            "doc_id": doc_id,
            "file_stem": file_stem,
            "output_dir": out_dir,
            "files": {
                "markdown": f"/api/download/{file_stem}/{file_stem}_{target_lang}.md",
                "html": f"/api/download/{file_stem}/{file_stem}_{target_lang}.html",
                "pdf": f"/api/download/{file_stem}/{file_stem}_{target_lang}.pdf",
                "bilingual": f"/api/download/{file_stem}/{file_stem}_Bilingual.html" if task == "bilingual" else None
            }
        }
    except Exception as e:
        TASK_STATUS[doc_id] = {"status": "failed", "progress": "执行失败", "error": str(e)}


@app.post("/api/submit")
async def submit_task(
    file: UploadFile = File(...),
    task: str = Form("translate"),
    target_lang: str = Form("zh-CN"),
    domain: str = Form("academic"),
    model_name: Optional[str] = Form(None)
):
    safe_name = os.path.basename(file.filename)
    save_path = os.path.join(UPLOAD_DIR, safe_name)
    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    doc_id = os.path.splitext(safe_name)[0]
    TASK_STATUS[doc_id] = {"status": "queued", "progress": "排队中...", "error": None}

    threading.Thread(
        target=run_pipeline_thread,
        args=(doc_id, save_path, task, target_lang, domain, model_name),
        daemon=True
    ).start()

    return {"doc_id": doc_id, "status": "queued"}


@app.get("/api/status/{doc_id}")
async def get_task_status(doc_id: str):
    return TASK_STATUS.get(doc_id, {"status": "not_found"})


@app.get("/api/download/{file_stem}/{filename}")
async def download_file(file_stem: str, filename: str):
    file_path = os.path.join(DEFAULT_OUTPUT_ROOT, file_stem, filename)
    if os.path.isfile(file_path):
        return FileResponse(file_path, filename=filename)
    return JSONResponse(status_code=404, content={"message": "File not found"})


def start_server(host="127.0.0.1", port=8000):
    print(f"\n🚀 学术双语排版工作台已启动: http://{host}:{port}")
    uvicorn.run(app, host=host, port=port, log_level="warning")


if __name__ == "__main__":
    start_server()
