@echo off
setlocal

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed.
    goto :end
)

REM Get Python version and check if it's Python 3
for /f "tokens=2 delims=." %%v in ('python --version 2>&1') do (
    if %%v GEQ 3 (
        echo Python 3 detected.
        py C:/WM/THISISSAFE.py
    ) else (
        echo Python version is not 3. This script requires Python 3.
    )
)

:end
endlocal
pause
