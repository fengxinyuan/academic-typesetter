@echo off
chcp 65001 >nul
title AcademicTypesetter - 学术文献智能翻译与出版排版系统
cd /d "%~dp0"

echo =====================================================================
echo  AcademicTypesetter: 学术文献智能翻译与出版排版系统
echo =====================================================================
echo.
echo  [1] 启动可视化 Web 双语工作台 (推荐)
echo  [2] 检查系统环境、浏览器与字体配置 (info)
echo  [3] 命令行处理任意文献/论文/专著 (process)
echo  [4] 退出
echo.
set /p choice="请输入选项 [1-4] (默认 1): "
if "%choice%"=="" set choice=1

if "%choice%"=="1" (
    echo.
    echo 正在启动 Web 工作台并打开浏览器...
    start http://127.0.0.1:8000
    python main.py serve
) else if "%choice%"=="2" (
    echo.
    python main.py info
    pause
) else if "%choice%"=="3" (
    echo.
    set /p input_pdf="请输入待处理的 PDF 文件路径: "
    if not "%input_pdf%"=="" (
        python main.py process "%input_pdf%" --task bilingual
    ) else (
        echo [WARN] 未输入有效文件路径！
    )
    pause
) else (
    exit
)
