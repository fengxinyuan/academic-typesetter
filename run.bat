@echo off
chcp 65001 >nul
title Matrix Theory Book Typesetter & Translator
cd /d "%~dp0"
echo =========================================================
echo  Matrix Theory (2nd Ed) Typesetting & Translation System
echo =========================================================
echo.
python run_llm_page_typesetter.py
echo.
echo Finished!
pause
