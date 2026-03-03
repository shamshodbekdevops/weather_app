"""
Django settings for core project.
"""

import importlib.util
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


def load_dotenv(dotenv_path):
    if not dotenv_path.exists():
        return

    for raw_line in dotenv_path.read_text(encoding='utf-8').splitlines():
        line = raw_line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue

        key, value = line.split('=', 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


def get_env(name, default=''):
    return os.environ.get(name, default)


load_dotenv(BASE_DIR / '.env')
HAS_WHITENOISE = importlib.util.find_spec('whitenoise') is not None


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env('SECRET_KEY', 'django-insecure-development-key-change-in-production')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_env('DEBUG', 'False').lower() == 'true'

# Railway.app uchun ALLOWED_HOSTS sozlamalari
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '.railway.app',
    'localhost:8000',
    '8000-localhost',
]

# .env fayldan ALLOWED_HOSTS qo'shish
extra_hosts = get_env('ALLOWED_HOSTS', '')
if extra_hosts:
    ALLOWED_HOSTS.extend([host.strip() for host in extra_hosts.split(',') if host.strip()])

railway_public_domain = get_env('RAILWAY_PUBLIC_DOMAIN', '').strip()
if railway_public_domain:
    ALLOWED_HOSTS.append(railway_public_domain)

ALLOWED_HOSTS = list(set(ALLOWED_HOSTS))  # Dublikatlarni olib tashlash


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'weather',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if HAS_WHITENOISE:
    MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

# CSRF trusted originlar (DEBUG holatidan qat'i nazar)
CSRF_TRUSTED_ORIGINS = [
    'https://*.railway.app',
    'https://*.up.railway.app',
    'http://127.0.0.1:8000',
    'http://localhost:8000',
]

if railway_public_domain:
    CSRF_TRUSTED_ORIGINS.append(f'https://{railway_public_domain}')

# Production sozlamalari
if not DEBUG:
    SECURE_SSL_REDIRECT = False  # Railway SSL proxy orqali ishlaydi
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# Railway PostgreSQL yoki local SQLite
DATABASE_URL = get_env('DATABASE_URL', '')
if DATABASE_URL:
    # PostgreSQL (Railway production)
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=600)
    }
else:
    # SQLite (local development)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

if HAS_WHITENOISE:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    # WhiteNoise'ni gzip qilishga ruxsat beramiz
    WHITENOISE_COMPRESSION_OFFLINE = True
    WHITENOISE_MIMETYPES = {
        '.js': 'application/javascript',
        '.css': 'text/css',
    }

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


OPENWEATHER_API_KEY = get_env('OPENWEATHER_API_KEY')

# Session sozlamalari (Cookie-based for Railway compatibility)
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
SESSION_COOKIE_AGE = 86400  # 24 soat
SESSION_SAVE_EVERY_REQUEST = True  # Har so'rovda session yangilansin
SESSION_COOKIE_HTTPONLY = True  # XSS himoyasi
SESSION_COOKIE_SAMESITE = 'Lax'  # CSRF himoyasi
