"""
Django settings for playtube project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv(override=True)  # Load environment variables from .env file


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.getenv('DEBUG')))

ALLOWED_HOSTS = str(os.getenv('ALLOWED_HOSTS')).split(
    ',') if not DEBUG else ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'play.apps.PlayConfig',
    'play.templatetags',
    'rest_framework',
    'corsheaders',
    'utm_tracker',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ]
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'utm_tracker.middleware.DetectBotsMiddleware',
    'utm_tracker.middleware.VisitsTrackerMiddleware',
]

ROOT_URLCONF = 'playtube.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates') 
        ],
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

WSGI_APPLICATION = 'playtube.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-in'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True

# Login redirect
LOGIN_URL = 'play:login'

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = str(os.getenv('EMAIL_HOST_USER'))
EMAIL_HOST_PASSWORD = str(os.getenv('EMAIL_HOST_PASSWORD'))
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = f'PlayTube <{EMAIL_HOST_USER}>'

# Server email
SERVER_EMAIL = f'PlayTube <{EMAIL_HOST_USER}>'
ADMINS = [('Admin', os.getenv('ADMIN_EMAIL'))]
MANAGERS = ADMINS

# CORS settings
CORS_ALLOW_ALL_ORIGINS = bool(int(os.getenv('CORS_ALLOW_ALL_ORIGINS', 0)))
CORS_ALLOWED_ORIGINS = str(os.getenv(
    'CORS_ALLOWED_ORIGINS')).split(',') if not CORS_ALLOW_ALL_ORIGINS else []

# Broken link email ignore list
IGNORABLE_404_URLS = [
    r'^/apple-touch-icon.*\.png$',
    r'^/favicon\.ico$',
    r'^/robots\.txt$',
    r'^/sitemap\.xml$',
    r'^/ads\.txt$',
    r'^/google.*\.html$',
    r'^/BingSiteAuth\.xml$',
    r'^/yandex_.*\.html$',
    r'^/.*\.txt$',
    r'^/.*\.xml$',
    r'^/.*\.json$',
    r'^/.*\.css$',
    r'^/.*\.js$',
    r'^/.*\.jpg$',
    r'^/.*\.jpeg$',
    r'^/.*\.png$',
    r'^/.*\.gif$',
    # in one line
    # r'^/(apple-touch-icon.*\.png|favicon\.ico|robots\.txt|sitemap\.xml|ads\.txt|google.*\.html|BingSiteAuth\.xml|yandex_.*\.html|.*\.txt|.*\.xml|.*\.json|.*\.css|.*\.js|.*\.jpg|.*\.jpeg|.*\.png|.*\.gif)$',
    '/HNAP1/',
    '/onvif/device_service',
    'PSIA/index',
] if DEBUG else []

# Logging settings
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "handlers": {
        "file": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": "logs/error.log",
            "formatter": "verbose",
        },
        "console": {
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
            "include_html": True,
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "file"],
            "propagate": True,
        },
        "django.request": {
            "handlers": ["mail_admins", "file"],
            "level": "ERROR",
            "propagate": False,
        },
    },
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = 'media/'

STATICFILES_DIR = [
    BASE_DIR / 'static'
]

MEDIA_ROOT = BASE_DIR / 'media'
STATIC_ROOT = BASE_DIR / 'static'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# IP address of the server
IP_ADDRESS = str(os.getenv('IP_ADDRESS'))

# Domain name of the server
DOMAIN_NAME = str(os.getenv('DOMAIN_NAME', IP_ADDRESS))

# Use HTTPS or not
USE_HTTPS = bool(int(os.getenv('USE_HTTPS', 0)))
SECURE_SSL_REDIRECT = False # set to True in production if not handled by reverse proxy
SESSION_COOKIE_SECURE = USE_HTTPS
CSRF_COOKIE_SECURE = USE_HTTPS
CSRF_TRUSTED_ORIGINS = str(os.getenv('CSRF_TRUSTED_ORIGINS')).split(',') if not DEBUG else []

# Celery settings
CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"


# AWS S3 settings
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.getenv('AWS_REGION')
AWS_DEFAULT_ACL = 'public-read'
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com'
AWS_S3_SIGNATURE_VERSION = 's3v4'
