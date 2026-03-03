#!/bin/bash
# Django Weather App - Local Setup Script (macOS/Linux)
# Lokal'da o'rnatish va ishga tushirish uchun skript

echo ""
echo "==========================================="
echo "Django Weather App - Local Setup"
echo "==========================================="
echo ""

# Python tekshirish
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python o'rnatilmagan!"
    echo "   https://python.org'dan Python 3.12+ o'rnating"
    exit 1
fi

echo "✅ Python topildi"
echo ""

# Virtual environment yaratish
echo "⏳ Virtual environment yaratilmoqda..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "❌ Error: Virtual environment yaratib bo'lmadi"
    exit 1
fi
echo "✅ Virtual environment yaratildi"
echo ""

# Virtual environment'ni aktivlash
source venv/bin/activate

# Requirements o'rnatish
echo "⏳ Dependencies o'rnatilmoqda..."
pip install -q -r requirements.txt
if [ $? -ne 0 ]; then
    echo "❌ Error: Dependencies o'rnatib bo'lmadi"
    exit 1
fi
echo "✅ Dependencies o'rnatildi"
echo ""

# Migrations o'tkazish
echo "⏳ Database migrations o'tkazilmoqda..."
python manage.py migrate --noinput
if [ $? -ne 0 ]; then
    echo "❌ Error: Migrations xatosi"
    exit 1
fi
echo "✅ Migrations o'tkazildi"
echo ""

# Static files yig'ish
echo "⏳ Static files yig'ilmoqda..."
python manage.py collectstatic --noinput --clear
if [ $? -ne 0 ]; then
    echo "❌ Error: Static files yig'ibob bo'lmadi"
    exit 1
fi
echo "✅ Static files yig'ildi"
echo ""

# Server ishga tushirish
echo ""
echo "==========================================="
echo "✅ TAYYOR - Server ishga tushurilmoqda..."
echo "==========================================="
echo ""
echo "🌐 Web: http://127.0.0.1:8000"
echo "🔧 Admin: http://127.0.0.1:8000/admin/"
echo ""
echo "⛔ Serverni to'xtatish uchun: CTRL+C"
echo ""

python manage.py runserver 0.0.0.0:8000
