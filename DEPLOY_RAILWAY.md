# Railway.app Deploy Qilish Bo'yicha Qo'llanma

## Qisqa Yo'l (5 minut ichida)

### 1. GitHub Repository'ni Tayyorlash
```bash
git init
git add .
git commit -m "Initial commit: Django weather app for Railway deployment"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/WeatherAPPNew.git
git push -u origin main
```

### 2. Railway.app'da Proyekt Yaratish
1. https://railway.app ga o'ting
2. GitHub bilan login qiling yoki sign up qiling
3. Dashboard'da "+ New Project" tugmasini bosing
4. "Deploy from GitHub repo" ni tanlang
5. YOUR_USERNAME/WeatherAPPNew repository'ni tanlang
6. Railway avtomatik detect qiladi va deploy qilishni boshlaydi

### 3. Environment Variables'larni Sozlash
Railway dashboard'da:

1. **PROJECT SETTINGS** → **Variables** bo'limiga o'ting
2. Quyidagi variable'larni qo'shing:

| Variable | Qiymat |
|----------|--------|
| `SECRET_KEY` | `django-insecure-aXvZ9k$L2mQpRtY%8nWxBj@5hGc#1dE4fS+3qU6vIoPw` (yangi, xavfsiz!) |
| `OPENWEATHER_API_KEY` | Sizning OpenWeather API key'ingiz |
| `DEBUG` | `False` |

### 4. Deployment Tekshirish
- Deployment logs'ni ko'ring - hamma yashil bo'lishi kerak ✅
- `https://<YOUR-APP>.railway.app` linkni bosing
- Hava ko'rsatilishi kerak

---

## To'liq Qo'llanma

### A. OpenWeather API Kalit Olish (Agar yo'q bo'lsa)

1. https://openweathermap.org/api'ga o'ting
2. Sign up qiling (Bepul)
3. API keys bo'limiga o'ting
4. "Default" API kalit'ni ko'ching (ko'nib turang!)
5. `.env` fayliga joylashtiring

### B. Local Tekshirish (Isroflash Bo'yicha)

```bash
# Virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# yoki
venv\Scripts\activate     # Windows

# Dependencies
pip install -r requirements.txt

# Migrations
python manage.py migrate

# Static files
python manage.py collectstatic --noinput

# Run
python manage.py runserver
# http://127.0.0.1:8000 ga o'ting
```

### C. Git'ga Push Qilish

```bash
git add .
git commit -m "Production ready setup"
git push
```

### D. Railway.app'da Deploy Qilish (Bosqichma-bosqich)

#### **1-Qadam: Railway.app'da Login**
- https://railway.app
- GitHub bilan login qiling

#### **2-Qadam: Yangi Proyekt**
- "+ New Project" → "Deploy from GitHub repo"
- YOUR_USERNAME/WeatherAPPNew ni tanlang

#### **3-Qadam: Environment Variables**
Quyidagi bo'limga o'ting: `Project Settings` → `Variables`

```
SECRET_KEY=django-insecure-<YANGI-KA-CHISM-KALIT>
OPENWEATHER_API_KEY=<SIZNING-API-KALIT>
DEBUG=False
```

#### **4-Qadam: Database (Ixtiyoriy)**
Default SQL Lite ishlatiladi - o'zgartirishga kerak yo'q

#### **5-Qadam: Deploy!**
Railway avtomatik deploy qiladi. Bir kaç menut kutib turing

#### **6-Qadam: Test**
- Deployment logs'ni ko'ring
- `https://<APP-NAME>.railway.app` linkni bosing

---

## Yangi SECRET_KEY Yaratish

Production uchun yangi SECRET_KEY kerak:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Chiqadigan qiymatni `SECRET_KEY` variable'iga qo'ying.

---

## Troubleshooting

### ❌ "502 Bad Gateway" xatosi
```bash
# 1. Logs'ni ko'ring
railway logs

# 2. Variable'larni tekshiring (SECRET_KEY, API_KEY)
# 3. Migrations'ni tekshiring
```

### ❌ Hava ko'rsatilmadi
- OPENWEATHER_API_KEY to'g'ri ko'chirilganini tekshiring
- API key aktiv bo'lganini tekshiring (openweathermap.org'da)

### ❌ Server xatosi
```bash
# Local test qiling
python manage.py runserver

# Debug = True qilib test qiling
DEBUG=True python manage.py runserver
```

---

## Bir Komanda bilan Deploy (Advanced)

Terminal'da:
```bash
# Git setup
git init
git add .
git commit -m "Ready for Railway"
git remote add origin https://github.com/YOUR_USERNAME/WeatherAPPNew.git
git push -u origin main

# Railway CLI bilan deploy (opsiyonal)
# https://docs.railway.app/guides/cli'ni o'qing
railway up
```

---

## Foydalanadi Ekran

✅ **Local:** http://127.0.0.1:8000  
✅ **Production:** https://your-app.railway.app

---

## Xapsizlik Tc'ki

- [ ] .env .gitignore'da (bu MUHIM!)
- [ ] SECRET_KEY yangilanishi (yangi kalit)
- [ ] DEBUG = False production'da
- [ ] API keys Railway variables'da sozlangan
- [ ] HTTPS ishlayotgan (Railway avtomatik)

---

## Qo'shimcha Resurslar

- [Django Deployment Docs](https://docs.djangoproject.com/en/5.2/howto/deployment/)
- [Railway Docs](https://docs.railway.app/)
- [OpenWeather API](https://openweathermap.org/api)
- [Gunicorn Docs](https://gunicorn.org/)

---

**Ishora:** Agar muammolar bo'lsa, GitHub issues'ni o'chiring yoki Railway support'ni bosing!
