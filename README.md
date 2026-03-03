# Django Weather Application

Bitta monolithic Django service sifatida ishlaydigan ob-havo ilovasi. Frontend va backend bir joyda - bitta URL orqali ishlaydi.

## Xususiyatlari

- 🌡️ Joriy ob-havo ma'lumotlari
- 💨 Havo ifloslanish indeksi
- 📅 5 kunlik prognoz
- 🌍 OpenWeather API bilan integratsiya
- 📱 Responsive dizayn

## Lokal ishga tushirish

### Talablar
- Python 3.12+
- pip

### O'rnatish

1. Repository klonlash:
```bash
git clone <repo-url>
cd WeatherAPPNew
```

2. Virtual environment yaratish:
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. Paketlarni o'rnatish:
```bash
pip install -r requirements.txt
```

4. .env faylini xatolik qilish:
```bash
# .env fayl allaqachon mavjud bo'lib, oldindan sozlangan
# Kerak bo'lsa quyidagi qiymatlarni o'zgartiring:
# - SECRET_KEY (development uchun - o'zgartirilishi tavsiya etiladi)
# - OPENWEATHER_API_KEY (OpenWeather API kalit)
# - DEBUG (local test uchun True)
```

5. Database migratsiyasini o'tkazish:
```bash
python manage.py migrate
```

6. Staticfiles'larini yig'ish (ixtiyoriy, local uchun):
```bash
python manage.py collectstatic --noinput
```

7. Development serverini ishga tushirish:
```bash
python manage.py runserver
```

Brauzeringizda http://127.0.0.1:8000 ga o'ting

## Railway.app'ga Deploy Qilish

### Oldindan tayyorlash

1. Repository'ni GitHub'ga push qilish:
```bash
git add .
git commit -m "Deploy uchun tayyor"
git push origin main
```

2. Railway.app'da akkaunt yaratish va login qilish: https://railway.app

### Deploy qilish

1. Railway.app'da yangi proyekt yaratish
2. GitHub repository'ni ulash
3. Environment variables'larni sozlash:
   - `SECRET_KEY` - yangi secure kalit yaratish: 
     ```python
     from django.core.management.utils import get_random_secret_key
     print(get_random_secret_key())
     ```
   - `OPENWEATHER_API_KEY` - OpenWeather API kalitingiz
   - `DEBUG` - `False` o'rnatish (production)
   - `ALLOWED_HOSTS` - Bu kerak bo'lmasligi mumkin (*.railway.app allaqachon sozlangan)

4. Deployment ishga tushishi kutish (2-5 minut)

### Postdeploy tekshirish

- `https://<your-app>.railway.app` ga o'ting
- Hava ma'lumotlari yuklansini tekshiring
- Turli shaharlarni qidirish nasazlarini tekshiring

## Proyekt Strukturasi

```
WeatherAPPNew/
├── core/                 # Django proyekt parametrlari
│   ├── settings.py      # Proyekt sozlamalari
│   ├── urls.py          # URL yo'naltirilishi
│   ├── wsgi.py          # WSGI app
│   └── asgi.py          # ASGI app
├── weather/             # Weather app
│   ├── views.py         # Django views
│   ├── urls.py          # App URL parametrlari
│   ├── models.py        # Database modellari
│   └── migrations/      # Database migratsiyalari
├── templates/           # HTML shablonlari
│   ├── base.html
│   ├── current_weather.html
│   ├── air_pollution.html
│   └── five_day_forecast.html
├── static/              # CSS, JavaScript, rasmlar
├── manage.py            # Django CLI
├── db.sqlite3          # SQLite database (local)
├── requirements.txt     # Python dependency'lari
├── Procfile            # Heroku/Railway deployment config
├── runtime.txt         # Python versiyasi
└── .env                # Environment variables
```

## Environment Variables

| Variable | Tasnifi | Misol |
|----------|---------|-------|
| SECRET_KEY | Django secret key (must be secret!) | `django-insecure-...` |
| OPENWEATHER_API_KEY | OpenWeather API kalit | `259afab76ef42...` |
| DEBUG | Debug mode (False production uchun) | `True` / `False` |
| ALLOWED_HOSTS | Ruxsat etilgan hostlar | `127.0.0.1,localhost,.railway.app` |

## OpenWeather API Kalit Olish

1. https://home.openweathermap.org/users/sign_up ga o'ting
2. Akkaunt yaratish
3. API keys bo'limiga o'ting
4. Default API kalitingizni ko'ching
5. `.env` faylining `OPENWEATHER_API_KEY` qiymatiga joylashtiring

## Troubleshooting

### "ModuleNotFoundError" xatosi
```bash
pip install -r requirements.txt
```

### Static files'lar yuklonmadi
```bash
python manage.py collectstatic --clear --noinput
```

### Database xato
```bash
python manage.py migrate
```

### Railway'da "502 Bad Gateway"
- Logs'ni tekshiring: `railway logs`
- Environment variable'larni tekshiring
- SECRET_KEY o'zgartirilganini tasdiqlang

## Xavfsizlik

?⚠️ **MUHIM:**
- Production'da `DEBUG = False` o'rnatish
- SECRET_KEY'ni hech qachon commit qilmang (`.env` allaqachon `.gitignore`'da)
- Production API key'larini Railway environment'da sozlang, kodda emas
- HTTPS orqali faqat ishlang

## Litsenziya

Licensed under MIT

## Yordam

Muammolar yoki savollar bovlda GitHub Issue yarating.

