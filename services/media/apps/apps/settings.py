"""
Django settings for apps project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import environ
import os
from django.conf.global_settings import FIXTURE_DIRS
from pathlib import Path
import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# ENVIRONT
env = environ.Env(
    DEBUG=(bool, True),
)

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = [
    '*'
]

TESTING = "test" in sys.argv

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #apps
    'uploader',

    #third
    'django_extensions',
    'rest_framework',
    "rest_framework.authtoken",
    "rest_framework_simplejwt",
    'rest_framework_simplejwt.token_blacklist',
]
if not TESTING:
    INSTALLED_APPS+= [
        "debug_toolbar",
    ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # thirds
]
if not TESTING:
    MIDDLEWARE+= [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

ROOT_URLCONF = 'apps.urls'

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

WSGI_APPLICATION = 'apps.wsgi.application'

APPEND_SLASH = True

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
        'NAME': env('DB_NAME'),
        'USER': env('DB_USERNAME'),
        'PASSWORD': env('DB_PASSWORD'),
        'STRICT_TRANS_TABLES': True,
        'STRICT_ALL_TABLES': True,
        'sql_mode': 'traditional',
        # 'OPTIONS': {
        #     'ssl_mode': 'DISABLED'
        # }
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True

USE_TZ = True

APP_URL=env('APP_URL')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

FIXTURE_DIRS = [
    os.path.join(BASE_DIR, 'fixtures'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
    "version": 1,  # the dictConfig format version
    "disable_existing_loggers": False,  # retain the default loggers
    "loggers": {
        "": { # "" str empty, indicite will be apply in global scope include third lib
            "level": "DEBUG",
            "handlers": ["file"],
        },
    },
    "formatters": {
        "verbose": {
            "format": "{name} {levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "filename": "general.log",
            "formatter": "verbose",
        },
    }
}

REST_FRAMEWORK  = {
    'DEFAULT_AUTHENTICATION_CLASSES' : [
        # 'rest_framework_simplejwt.authentication.JWTAuthentication', # disable due use custombaseauth class for kong
        'config.rest_framework.auth.CustomBaseAuth',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication', # this module neeede for default auth djano, in section is django temporray login and logout
        'rest_framework.authentication.TokenAuthentication', # way to know avaible auth type: open https://www.django-rest-framework.org/api-guide/authentication/#setting-the-authentication-scheme and rest_xxx.autxxx.{List of APIReference}
    ],
    'DEFAULT_RENDERER_CLASSES' : [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated', # any route who access must login
        'rest_framework.permissions.AllowAny',
    ],
    # https://www.django-rest-framework.org/api-guide/throttling/
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    # 'DEFAULT_THROTTLE_RATES': {
    #     'anon': '10000/day', # test for login view
    #     'user': '10000/day',
    #     'login-attempt' : '2/minute', # look user_app.throttling.LoginThrottle
    #     'register-attempt' : '10/minute',
    # },
    # 'TEST_REQUEST_RENDERER_CLASSES': [
    #     # 'rest_framework.renderers.MultiPartRenderer',
    #     'rest_framework.renderers.JSONRenderer',
    #     # 'rest_framework.renderers.TemplateHTMLRenderer'
    # ]

    # for default setting on generic and viewset view, if want on APIView to apply see https://stackoverflow.com/questions/35830779/django-rest-framework-apiview-pagination
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination', # "next": "http://127.0.0.1:8000/watch/stream/review/filter/?limit=4&offset=4&username=admin",
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.CursorPagination', # http://127.0.0.1:8000/watch/stream/review/filter/?cursor=cD0yMDIzLTA3LTIzKzA4JTNBMTIlM0E0Mi44NTg2NzYlMkIwMCUzQTAw&username=admin
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination', # http://127.0.0.1:8000/watch/stream/review/filter/?page=2&username=admin
    # 'PAGE_SIZE': 4
}

# SAFE_DELETE
SAFE_DELETE_FIELD_NAME = 'deleted_at'

# DJANGO TOOLBAR
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

# KONG
KONG_HOST_API= env('KONG_HOST_API')
KONG_HOST_PORT= env('KONG_HOST_PORT')
