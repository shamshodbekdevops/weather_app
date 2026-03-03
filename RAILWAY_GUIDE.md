# Railway.app Deployment Guide (Uzbek) 🚀

## Senior Qo'llanma

Sizning Django Weather App'ingiz **bitta monolithic service** sifatida Railway.app'ga deploy qilish uchun to'liq qo'llanma.

---

## 📋 Oldindan Tayyorlash

### ✅ 1-qadam: GitHub'da Repository Yaratish

```bash
# Lokal'da
cd d:\30_Projects\WeatherAPPNew

# Git'ni initialize qilish
git init

# Barcha fayllarni add qilish
git add .

# Commit qilish
git commit -m "Django Weather App - Production ready for Railway"

# GitHub'da repository yaratish (https://github.com/new)
# Shunga qo'sh:
git remote add origin https://github.com/YOUR_USERNAME/WeatherAPPNew.git
git branch -M main
git push -u origin main
```

---

## 🚀 Railway'da Deploy Qilish

### Qadam 1: Railway.app Registration

1. **https://railway.app** ga o'chish
2. **"Continue with GitHub"** tugmasini bosish
3. GitHub credentials'ni kiriting
4. GitHub izni berish (authorize)

### Qadam 2: Yangi Proyekt Yaratish

1. Railway Dashboard'da bo'ling
2. **"+ New Project"** tugmasini bosing
3. **"Deploy from GitHub repo"** ni tanlang
4. GitHub permissions berilsa, repo ro'yxatini ko'rasiz
5. **WeatherAPPNew** repository'ni tanlang
6. Railway avtomatik deploy qilishni boshlaydi ✅

### Qadam 3: Environment Variables Sozlash

Deploy boshlanganda, Railway sizga **Environment** bo'limga o'tishni taklif qiladi:

#### Qo'shish kerak bo'lgan Variables:

| Variable Name | Value | Izoh |
|---|---|---|
| `SECRET_KEY` | `django-insecure-...` (yangi!) | [Shi'rzo qarang](#yangi-secret-key-yaratish) |
| `OPENWEATHER_API_KEY` | `259afab76ef42e09f450458b74b2f279` | Sizning OpenWeather kalit'ingiz |
| `DEBUG` | `False` | **Production uchun MUHIM!** |
| `ALLOWED_HOSTS` | `*.railway.app,localhost` | Railway domenlari |

#### Vizual Bo'yicha:
```
Settings → Variables → Qo'shish

SECRET_KEY = [yangi kalit kiritish]
OPENWEATHER_API_KEY = [API kalit kiritish]
DEBUG = False
ALLOWED_HOSTS = *.railway.app,localhost
```

### Qadam 4: Deploy Tugmachini Bosing

1. Variables'ni saqlash
2. **"Deploy"** tugmasini bosing
3. Logs'ni kuzatish (ko'k log = yaxshi 👍)

### Qadam 5: Production Domain Olish

Deploy tugallangach:
- Railway avtomatik domain beradi: `https://<PROJECT-NAME>.railway.app`
- Brauzeringizda bu linkni ochmang va test qiling
- **Hava ma'lumotlari ko'rsatilishi kerak!** 🌡️

---

## 🔑 Yangi SECRET_KEY Yaratish

Production uchun yangi xavfsiz kalit kerak:

### Variant 1: Lokal'da (Tavsiya)
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Variant 2: Python REPL'da
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Barcha qiymatni ko'ching va **SECRET_KEY** variable'iga qo'ching.

---

## 📱 OpenWeather API Kalit Olish

Agar hali bo'lmasa:

1. **https://openweathermap.org/users/sign_up** ga o'ting
2. Akkaunt yaratish (bepul)
3. Email tasdiqlash
4. **API Keys** bo'limiga o'ting
5. **Default** kalitni ko'ching
6. Railway **OPENWEATHER_API_KEY** variable'iga qo'ching

---

## ✅ Deploy Muvaffaqiyatlik Tekshirish

### ✅ Hamma Yashil Bo'lishi Kerak:

| Belgi | Nima |
|------|------|
| ✅ | Railway logs'da xato bo'lmasligi |
| ✅ | App URL'ga o'chiladigan vaqti |
| ✅ | Yangi shahar qidiriladigan vaqti |
| ✅ | Hava ma'lumotlari ko'rsatilganda |
| ✅ | Admin panel `/admin/` ishlatganda |

### ❌ Agar Muammolar Bo'lsa:

```bash
# Railway CLI bilan logs ko'rish (opsiyonal)
npm install -g @railway/cli
railway login
railway logs

# Yoki: Railway Dashboard → Project → Logs
```

---

## 🔧 Production Sozlamalari (Mavjud)

Biz allaqachon o'zgartirdik:

✅ `Procfile` - release va web commands  
✅ `runtime.txt` - Python 3.12.3  
✅ `requirements.txt` - Barcha paketlar  
✅ `settings.py` - ALLOWED_HOSTS, CSRF, SECURE sozlamalari  
✅ `.env` - Local development sozlamalari  

---

## 📊 Proyekt Struktura (Railway uchun optimal)

```
WeatherAPPNew/
├── core/                    ← Django settings
├── weather/                 ← Weather app
├── templates/               ← HTML (frontend)
├── static/                  ← CSS, JS (frontend asset'lari)
├── manage.py               ← Django CLI
├── Procfile                ← Railway deploy commands
├── runtime.txt             ← Python version
├── requirements.txt        ← Python dependencies
├── .env                    ← Local variables
├── .gitignore             ← Git exclude
├── README.md              ← Documentation
└── DEPLOY_RAILWAY.md      ← Bu qo'llanma
```

**Muhim:** Bu **bitta monolithic service**! Frontend va backend bir joyda `templates/` va `static/` fayllar Django orqali served.

---

## 🌐 Domenni Sozlash (Ixtiyoriy)

Agar o'zingizning domeni bo'lsa:

1. Railway → Settings → Domains
2. "+ Add Domain"
3. Sizning domain'ni kiriting
4. DNS sozlamalarni Railway'ning ko'rsatmasiga brigina sozlang
5. 15-30 minut kutib turing

---

## 🔒 Xavfsizlik Tc'ki

**⚠️ MUHIM TAQQOSLAMALAR:**

- [ ] `DEBUG = False` production'da set qilinganini tekshiring
- [ ] `.env` fayling `.gitignore`'da bo'lganini tekshiring (SECRET_KEY exposed bo'lmasin!)
- [ ] OpenWeather API key'i to'g'ri sozlangan
- [ ] HTTPS ishlayotganini tekshiring (Railway avtomatik SSL)
- [ ] CSRF_TRUSTED_ORIGINS'da Railway domain'lar mavjud
- [ ] Jismoniy database backup's (Railway da islmadi - SQLite noto'rtinchi)

---

## 🚨 Troubleshooting

### 502 Bad Gateway ❌

```bash
# Railway logs'da ko'rish
railway logs

# Tekshirish:
1. SECRET_KEY to'g'ri o'chirilganini
2. OPENWEATHER_API_KEY mavjudligini  
3. DEBUG = False ekanligini
4. gunicorn ishlatilganini (Procfile)
```

### Hava Datasi Ko'rsatilmadi ❌

```bash
# OpenWeather API:
1. API kalit to'g'ri
2. API kalit aktiv (openweathermap.org da)
3. Free plan suhifasi (40 so'rovga ishlatish cheklash)
4. Shahar nomini to'g'ri yozganingizni
```

### Static Files (CSS/JS) Ko'rsatilmadi ❌

```bash
# Railway da:
1. collectstatic allaqachon o'tganini tekshiring
2. Procfile bo'limda release command'ini tekshiring
```

---

## 💰 Railway Narxi

> Railway **$5/oy** free tier beradi

- **Birinchi 500 saat** ishlatish bepul
- Shunga qo'sh **100GB bandwidth** bepul
- Xotira: **8GB RAM** bepul tur'da
- Database: **SQLite local** (bepul)

Bu app uchun **hech qanday to'lovga kerak bo'lmasligi** kerak!

---

## 📞 Qo'shimcha Yordam

### Railway Documentation
- Railway Docs: https://docs.railway.app
- Pricing: https://railway.app/pricing
- Help: https://railway.app/support

### Django Documentation
- Django Deployment: https://docs.djangoproject.com/en/5.2/howto/deployment/

### OpenWeather
- API Docs: https://openweathermap.org/api
- Support: https://openweathermap.org/find/density

---

## 🎉 Tayyor!

Deploy tugallangach:

```
🌐 App URL: https://<PROJECT-NAME>.railway.app
🔧 Admin: https://<PROJECT-NAME>.railway.app/admin/
📍 Lokal: http://127.0.0.1:8000 (develop'da still)
```

**Congratulations! Django Weather App Railway'da live! 🚀**

---

*Last updated: March 3, 2026*
