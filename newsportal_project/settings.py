"""
Django settings for newsportal_project project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

from dotenv import load_dotenv, find_dotenv

# Настройка окружения
load_dotenv(find_dotenv('../.env'))



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-s=98sb+s#q8ltud!b=g8kvjuv6)ro!yj29_tho(roiu)mzs$j$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'style' : '{',
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
        'special': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'
        },
        'special_for_error': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s'
        },
        'general': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s'
        },
        'error': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s'
        },
        'security': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'special'
        },
        'console_error': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'special_for_error'
        },
        'file_general': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'formatter': 'general',
            'filename': 'general.log'
        },
        'file_error': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'formatter': 'error',
            'filename': 'errors.log'
        },
        'file_security': {
            'level': 'DEBUG',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'formatter': 'security',
            'filename': 'security.log'
        },
        'console_message_error': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'security',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'console_warning', 'console_error', 'file_general'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins', 'file_error', 'console_message_error'],
            'propagate': False,
        },
        'django.server': {
            'handlers': ['file_error'],
            'propagate': False,
        },
        'django.template': {
            'handlers': ['file_error'],
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['file_error'],
            'propagate': False,
        },
        'django.security': {
            'handlers': ['file_security'],
            'propagate': False,
        },
        'django.server': {
            'handlers': ['console_message_error'],
            'propagate': False,
        },
    }
}


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'newsportal_app',

    'django_apscheduler',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django.contrib.sites',
    'django.contrib.flatpages',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'allauth.account.middleware.AccountMiddleware'
]

ROOT_URLCONF = 'newsportal_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'newsportal_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'postgres',
#        'USER': 'postgres',
#        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
#        'HOST': 'localhost',
#        'PORT': '5432',
#    }
#}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

LANGUAGES = [
    ('en-us', 'English'),
    ('ru', 'Русский'),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [BASE_DIR / 'static']

# Настройка регистрации
LOGIN_URl = '/accounts/login/'
LOGIN_REDIRECT_URL = '/newspaper/main/'
LOGOUT_REDIRECT_URL = '/newspaper/'
SITE_URL = 'http://127.0.0.1:8000'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_FORMS = {'signup': 'newsportal_app.forms.BasicSignupForm'}

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APP": {
            "client_id": f"{os.getenv('CLIENT_ID')}",
            "secret": f"{os.getenv('SECRET')}",
        },
    },
}

# Настройка кэша
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'), # Указываем, куда будем сохранять кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
        'TIMEOUT': 30,
    }
}

# Настройка рассылки
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_USE_TLS = True
EMAIL_PORT = 2525
EMAIL_HOST_USER = f"{os.getenv('ACCOUNT_NAME')}"
EMAIL_HOST_PASSWORD = f"{os.getenv('ACCOUNT_PASSWORD')}"
DEFAULT_FROM_EMAIL = f"{os.getenv('ACCOUNT_NAME')}@mail.ru"

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25

# Настройка Celery
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
