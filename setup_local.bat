@echo off
REM Django Weather App - Local Setup Script (Windows)
REM Lokal'da o'rnatish va ishga tushirish uchun skript

echo.
echo ===========================================
echo Django Weather App - Local Setup
echo ===========================================
echo.

REM Python tekshirish
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python o'rnatilmagan!
    echo https://python.org'dan Python 3.12+ o'rnating
    pause
    exit /b 1
)

echo [✓] Python topildi
echo.

REM Virtual environment yaratish
echo [*] Virtual environment yaratilmoqda...
python -m venv venv
if errorlevel 1 (
    echo Error: Virtual environment yaratib bo'lmadi
    pause
    exit /b 1
)
echo [✓] Virtual environment yaratildi
echo.

REM Requirements o'rnatish
echo [*] Dependencies o'rnatilmoqda...
call venv\Scripts\pip install -q -r requirements.txt
if errorlevel 1 (
    echo Error: Dependencies o'rnatib bo'lmadi
    pause
    exit /b 1
)
echo [✓] Dependencies o'rnatildi
echo.

REM Migrations o'tkazish
echo [*] Database migrations o'tkazilmoqda...
call venv\Scripts\python manage.py migrate --noinput
if errorlevel 1 (
    echo Error: Migrations xatosi
    pause
    exit /b 1
)
echo [✓] Migrations o'tkazildi
echo.

REM Static files yig'ish
echo [*] Static files yig'ilmoqda...
call venv\Scripts\python manage.py collectstatic --noinput --clear
if errorlevel 1 (
    echo Error: Static files yig'ibob bo'lmadi
    pause
    exit /b 1
)
echo [✓] Static files yig'ildi
echo.

REM Server ishga tushirish
echo.
echo ===========================================
echo [✓] TAYYOR - Server ishga tushurilmoqda...
echo ===========================================
echo.
echo Web: http://127.0.0.1:8000
echo Admin: http://127.0.0.1:8000/admin/
echo.
echo Serverni to'xtatish uchun: CTRL+C
echo.
pause

call venv\Scripts\python manage.py runserver 0.0.0.0:8000
