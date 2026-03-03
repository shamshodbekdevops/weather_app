# 🌤️ Django Weather Application

**Real-time ob-havo ma'lumotlari va havo sifatini kuzatish ilovasi**

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2-green.svg)](https://www.djangoproject.com/)
[![Railway](https://img.shields.io/badge/Deployed%20on-Railway-blueviolet.svg)](https://railway.app)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **🌐 Live Demo:** [https://shamshod-weather.up.railway.app](https://shamshod-weather.up.railway.app)

---

## 📋 Mundarija

- [Xususiyatlari](#-xususiyatlari)
- [Demo](#-demo-screenshots)
- [Texnologiyalar](#-texnologiyalar)
- [Lokal O'rnatish](#-lokal-ornatish)
- [Railway Deploy](#-railway-deploy)
- [API Konfiguratsiya](#-api-konfiguratsiya)
- [Loyiha Strukturasi](#-loyiha-strukturasi)
- [Xavfsizlik](#-xavfsizlik)
- [Contributing](#-contributing)
- [Litsenziya](#-litsenziya)

---

## ✨ Xususiyatlari

### 🌡️ **Joriy Ob-havo**
- Real-time harorat va his etilgan harorat
- Shamol tezligi va yo'nalishi
- Namlik va atmosfera bosimi
- Osmon holati (bulutlilik, yomg'ir, qor va h.k.)
- Mahalliy vaqt (timezone-aware)

### 💨 **Havo Ifloslanish Monitoringi**
- Air Quality Index (AQI) real-time
- PM2.5 va PM10 zarralar miqdori
- CO, NO₂, O₃, SO₂ gazlar konsentratsiyasi
- Niqob tavsiyalari AQI asosida
- Rang kodlangan xavf darajalari

### 📅 **5 Kunlik Prognoz**
- Kunlik minimal/maksimal harorat
- O'rtacha namlik
- Ob-havo tavsifi (o'zbekcha)
- Kun nomlari (o'zbekcha)
- Ikonali vizual ko'rinish

### 🎨 **Foydalanuvchi Tajribasi**
- Responsive dizayn (mobile, tablet, desktop)
- Bootstrap 5 UI framework
- Real-time shahar qidiruv
- Session-based shahar eslab qolish
- Xatoliklarni qulay ko'rsatish

---

## 🎥 Demo Screenshots

**Joriy Ob-havo Sahifasi**
```
🌐 https://shamshod-weather.up.railway.app/
```

**Havo Ifloslanish**
```
🌐 https://shamshod-weather.up.railway.app/pollution/
```

**5 Kunlik Prognoz**
```
🌐 https://shamshod-weather.up.railway.app/forecast/
```

---

## 🛠️ Texnologiyalar

### Backend
- **Django 5.2.7** - Python web framework
- **Gunicorn** - WSGI HTTP server (production)
- **Requests** - HTTP library for API calls
- **dj-database-url** - Database configuration

### Frontend
- **Bootstrap 5** - CSS framework
- **Django Templates** - Server-side rendering
- **Font Awesome** - Icons

### Database
- **SQLite** - Local development
- **PostgreSQL** - Production (Railway optional)
- **Cookie-based Sessions** - Railway-compatible

### API
- **OpenWeather API** - Weather data provider
  - Current Weather API
  - Air Pollution API
  - 5 Day Forecast API
  - Geocoding API

### Deployment
- **Railway.app** - Cloud platform
- **WhiteNoise** - Static files serving
- **GitHub** - Version control

---

## 🚀 Lokal O'rnatish

### Talablar
- Python 3.12 yoki yuqori
- pip (Python package manager)
- Git

### 1️⃣ Repository Klonlash

```bash
git clone https://github.com/shamshodbekdevops/weather_app.git
cd weather_app
```

### 2️⃣ Virtual Environment Yaratish

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Dependencies O'rnatish

```bash
pip install -r requirements.txt
```

### 4️⃣ Environment Variables Sozlash

`.env` fayli yaratish (yoki mavjud fayldagi qiymatlarni o'zgartirish):

```env
# Django Settings
SECRET_KEY=django-insecure-your-secret-key-here
DEBUG=True

# OpenWeather API
OPENWEATHER_API_KEY=your_api_key_here

# Allowed Hosts
ALLOWED_HOSTS=127.0.0.1,localhost
```

> **⚠️ Eslatma:** `.env` fayli `.gitignore`'da — hech qachon commit qilmang!

### 5️⃣ Database Migration

```bash
python manage.py migrate
```

### 6️⃣ Static Files Yig'ish

```bash
python manage.py collectstatic --noinput
```

### 7️⃣ Development Server Ishga Tushirish

```bash
python manage.py runserver
```

📱 **Brauzerda:** http://127.0.0.1:8000

---

## 🌐 Railway Deploy

### Quick Deploy (5 daqiqa)

1️⃣ **GitHub Repository Push:**
```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```

2️⃣ **Railway Setup:**
- [railway.app](https://railway.app) ga o'ting
- GitHub bilan login qiling
- "New Project" → "Deploy from GitHub repo"
- Repository tanlang: `weather_app`

3️⃣ **Environment Variables:**

Railway Dashboard → Variables:

| Variable | Value |
|----------|-------|
| `SECRET_KEY` | Yangi secure key ([generator](https://djecrety.ir/)) |
| `OPENWEATHER_API_KEY` | OpenWeather API key |
| `DEBUG` | `False` |
| `RAILWAY_PUBLIC_DOMAIN` | `shamshod-weather.up.railway.app` |

> 💡 **SECRET_KEY generatsiya qilish:**
> ```bash
> python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
> ```

4️⃣ **Deploy!**
- Railway avtomatik build va deploy qiladi
- Logs'ni kuzating
- App URL'ni oching

### PostgreSQL Qo'shish (Ixtiyoriy)

Railway → Add Service → PostgreSQL
- `DATABASE_URL` avtomatik sozlanadi
- Redeploy qiling

---

## 🔑 API Konfiguratsiya

### OpenWeather API Key Olish

1. [OpenWeatherMap](https://openweathermap.org/api) ga o'ting
2. Account yarating (bepul)
3. API Keys bo'limiga o'ting
4. Default API key'ni ko'ching
5. `.env` faylga qo'ying:
   ```env
   OPENWEATHER_API_KEY=your_api_key_here
   ```

### Limitlar (Free Plan)
- ✅ 60 calls/minute
- ✅ 1,000,000 calls/month
- ✅ Current weather
- ✅ 5 day forecast
- ✅ Air pollution data

---

## 📁 Loyiha Strukturasi

```
WeatherAPPNew/
├── 📂 core/                      # Django proyekt sozlamalari
│   ├── settings.py              # Asosiy konfiguratsiya
│   ├── urls.py                  # URL routing
│   ├── wsgi.py                  # WSGI entry point
│   └── asgi.py                  # ASGI entry point
│
├── 📂 weather/                   # Weather application
│   ├── views.py                 # Business logic
│   ├── urls.py                  # App URL patterns
│   ├── models.py                # Database models
│   ├── admin.py                 # Admin panel config
│   └── migrations/              # Database migrations
│
├── 📂 templates/                 # HTML templates
│   ├── base.html               # Base template
│   ├── current_weather.html    # Current weather view
│   ├── air_pollution.html      # Air pollution view
│   └── five_day_forecast.html  # Forecast view
│
├── 📂 static/                    # Static files (auto-created)
│   └── (CSS, JS, images)
│
├── 📂 staticfiles/               # Collected static files (production)
│
├── 📄 manage.py                  # Django CLI
├── 📄 requirements.txt           # Python dependencies
├── 📄 Procfile                   # Railway deployment config
├── 📄 runtime.txt                # Python version specification
├── 📄 .env                       # Environment variables (local)
├── 📄 .gitignore                 # Git ignore patterns
├── 📄 db.sqlite3                 # SQLite database (local)
└── 📄 README.md                  # Documentation (shu fayl)
```

---

## ⚙️ Environment Variables

### Local Development (.env)

```env
# Django Core
SECRET_KEY=django-insecure-your-secret-key-here
DEBUG=True

# OpenWeather API
OPENWEATHER_API_KEY=your_openweather_api_key

# Network
ALLOWED_HOSTS=127.0.0.1,localhost
```

### Production (Railway)

| Variable | Tavsif | Misol |
|----------|--------|-------|
| `SECRET_KEY` | Django secret key (50+ belgi) | `django-insecure-abc123...` |
| `OPENWEATHER_API_KEY` | OpenWeather API key | `259afab76ef42e09f45...` |
| `DEBUG` | Debug mode (FALSE!) | `False` |
| `RAILWAY_PUBLIC_DOMAIN` | Railway public domain | `shamshod-weather.up.railway.app` |
| `DATABASE_URL` | PostgreSQL URL (ixtiyoriy) | `postgresql://user:pass@...` |

---

## 🔧 Troubleshooting

### ❌ ModuleNotFoundError

**Sabab:** Dependencies o'rnatilmagan

**Yechim:**
```bash
pip install -r requirements.txt
```

---

### ❌ Static Files Yuklanmayapti

**Sabab:** Static files yig'ilmagan

**Yechim:**
```bash
python manage.py collectstatic --noinput --clear
```

---

### ❌ CSRF Verification Failed

**Sabab:** Railway domeni trusted origins'da yo'q

**Yechim:** Railway Variables'da qo'shing:
```
RAILWAY_PUBLIC_DOMAIN=shamshod-weather.up.railway.app
```

---

### ❌ Invalid API Key

**Sabab:** OpenWeather API key noto'g'ri yoki faol emas

**Yechim:**
1. [OpenWeatherMap](https://home.openweathermap.org/api_keys) ga o'ting
2. API key'ni tekshiring (faol bo'lishi kerak)
3. Railway Variables'da yangilash
4. Redeploy qiling

---

### ❌ 500 Internal Server Error

**Sabab:** Server xatosi (settings, database, yoki kod xatosi)

**Yechim:**
1. Railway Logs'ni tekshiring: `Deployments → Logs`
2. `DEBUG=True` (faqat test uchun!) qilib xatoni ko'ring
3. Error traceback asosida tuzatish

---

### ❌ Database Migration Error

**Sabab:** Migrations o'tkazilmagan

**Yechim:**
```bash
# Local
python manage.py migrate

# Railway (avtomatik - Procfile'da)
# Agar ishlamasa, Railway console'dan:
python manage.py migrate --noinput
```

---

## 🛡️ Xavfsizlik

### Production Checklist

- [x] `DEBUG = False` production'da
- [x] `SECRET_KEY` yangi va uzoq (50+ belgi)
- [x] `.env` fayling `.gitignore`'da
- [x] HTTPS (Railway avtomatik)
- [x] CSRF protection enabled
- [x] ALLOWED_HOSTS to'g'ri sozlangan
- [x] Secure cookies (production'da)
- [x] HSTS headers enabled

### API Key Xavfsizligi

- ⚠️ **Hech qachon** API key'ni GitHub'ga commit qilmang
- ✅ Environment variables ishlatish
- ✅ `.env` fayling `.gitignore`'da
- ✅ Railway'da Variables orqali sozlash
- ✅ OpenWeather free plan cheklovlarini bilish (60 req/min)

---

## 📊 Ishlash Metrikalari

### OpenWeather API Limitlar (Free Tier)

| Metric | Limit |
|--------|-------|
| Calls/Minute | 60 |
| Calls/Month | 1,000,000 |
| Response Time | ~200-500ms |
| Data Update | Har 10 daqiqa |

### Railway Resources (Free Tier)

| Resource | Limit |
|----------|-------|
| RAM | 512MB (default) |
| CPU | Shared |
| Bandwidth | 100GB/month |
| Deploy Time | ~2-5 daqiqa |

---

## 🔄 Update va Maintenance

### Kodni Yangilash

```bash
# 1. Lokal o'zgarishlar
git add .
git commit -m "Feature: yangi funksiya"

# 2. GitHub'ga push
git push origin main

# 3. Railway avtomatik deploy qiladi
# Logs'ni kuzatish: Railway Dashboard → Deployments
```

### Dependency Yangilash

```bash
# Dependencies'ni tekshirish
pip list --outdated

# Ma'lum paketni yangilash
pip install --upgrade django

# requirements.txt yangilash
pip freeze > requirements.txt
```

---

## 🤝 Contributing

Loyihaga hissa qo'shishni xohlaysizmi? Xush kelibsiz!

### Qadamlar:

1. **Fork** qiling
2. **Feature branch** yarating (`git checkout -b feature/YangiFunksiya`)
3. **Commit** qiling (`git commit -m 'Add: Yangi funksiya'`)
4. **Push** qiling (`git push origin feature/YangiFunksiya`)
5. **Pull Request** oching

### Code Style

- Python: PEP 8
- Django: Django Style Guide
- Comments: O'zbekcha yoki Inglizcha
- Naming: Snake_case (Python), kebab-case (HTML/CSS)

---

## 📝 To-Do / Roadmap

- [ ] User authentication & profiles
- [ ] Sevimli shaharlar ro'yxati
- [ ] Email/SMS xabarnomalar (haddan tashqari AQI)
- [ ] Historical weather data charts
- [ ] Multi-language support (🇺🇿 🇬🇧 🇷🇺)
- [ ] PWA (Progressive Web App)
- [ ] Dark mode theme
- [ ] Weather alerts & warnings
- [ ] UV Index tracking
- [ ] Hourly forecast (24 soatlik)

---

## 📚 Resurslar va Havolalar

### Dokumentatsiya
- [Django Docs](https://docs.djangoproject.com/)
- [OpenWeather API Docs](https://openweathermap.org/api)
- [Railway Docs](https://docs.railway.app/)
- [Bootstrap 5 Docs](https://getbootstrap.com/docs/5.3/)

### Qo'shimcha
- [Python Best Practices](https://docs.python-guide.org/)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/)
- [PEP 8 Style Guide](https://peps.python.org/pep-0008/)

---

## 📧 Aloqa

**Developer:** Shamshodbek  
**GitHub:** [@shamshodbekdevops](https://github.com/shamshodbekdevops)  
**Project:** [weather_app](https://github.com/shamshodbekdevops/weather_app)  
**Live Demo:** [shamshod-weather.up.railway.app](https://shamshod-weather.up.railway.app)

---

## 📜 Litsenziya

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2026 Shamshodbek

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## 🌟 Minnatdorchilik

- [OpenWeatherMap](https://openweathermap.org/) - Bepul weather API uchun
- [Railway](https://railway.app/) - Oson deployment uchun
- [Django Community](https://www.djangoproject.com/community/) - Ajoyib framework uchun
- [Bootstrap Team](https://getbootstrap.com/) - Responsive UI uchun

---

## ⭐ Star Us!

Agar bu loyiha sizga yoqsa, ⭐ **star** bosishni unutmang!

[![GitHub stars](https://img.shields.io/github/stars/shamshodbekdevops/weather_app?style=social)](https://github.com/shamshodbekdevops/weather_app)
[![GitHub forks](https://img.shields.io/github/forks/shamshodbekdevops/weather_app?style=social)](https://github.com/shamshodbekdevops/weather_app/fork)

---

<div align="center">

**Made with ❤️ in Uzbekistan 🇺🇿**

[🌐 Live Demo](https://shamshod-weather.up.railway.app) • [📖 Documentation](#) • [🐛 Report Bug](https://github.com/shamshodbekdevops/weather_app/issues) • [✨ Request Feature](https://github.com/shamshodbekdevops/weather_app/issues)

</div>

