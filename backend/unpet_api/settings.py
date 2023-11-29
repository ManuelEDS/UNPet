"""
Django settings for unpet_api project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    default="django-insecure-735@@_5xx-#aih%8o9x0zup&04ung1_dt31#deu(@xf62zo_&-",
)

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG=False
LOCAL_DB = False # DEBUG = True #para usar sqlite, FALSE para la db con las variables de entorno
DOCKER_MODE=False
RENDER_MODE = True

if DOCKER_MODE: # Modo: despliegue en algun seguidor docker (plan B por si render falla)
    ALLOWED_HOSTS = ['*']
    CORS_ALLOWED_ORIGINS = ['http://localhost', 'http://127.0.0.1', 'http://0.0.0.0']
    CSRF_TRUSTED_ORIGINS = ['http://localhost:81']
elif RENDER_MODE: # Modo: despliegue en render
    ALLOWED_HOSTS = ['*']
    CORS_ALLOWED_ORIGINS = ['https://unpet-web.onrender.com']
    CSRF_TRUSTED_ORIGINS = ['https://unpet-web.onrender.com']
    
    CORS_ORIGIN_WHITELIST = ['https://unpet-web.onrender.com']
    CORS_ALLOW_ALL_ORIGINS = True
else: # Modo: desarrollo en localhost
    ALLOWED_HOSTS = ['*']
    CORS_ALLOWED_ORIGINS = ['http://localhost', 'http://127.0.0.1', 'http://localhost:5173', 'http://127.0.0.1:5173']
    CSRF_TRUSTED_ORIGINS = ['http://localhost:5173', 'http://127.0.0.1:5173']
    CORS_ORIGIN_WHITELIST = ['http://localhost:5173', 'http://127.0.0.1:5173']
    CORS_ALLOW_ALL_ORIGINS = True

   
CORS_EXPOSE_HEADERS = ['Content-Type', 'X-CSRFToken', 'csrftoken']
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = [
    'csrftoken',
    'content-type',
    'origin',
    'x-allowed-headers',
    'x-csrftoken',
    'x-requested-with',
    'X-CSRFToken',
    # Agrega cualquier otro header que necesites permitir
]
# https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts
 # poner el de render react url

# Application definition

apps = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "rest_framework",
    "coreapi",
    "utils",
    "accounts",
    "pets",
    "posts",
    "search",
]

if not DOCKER_MODE:
    apps.append('corsheaders')

#if not RENDER_MODE:
#apps.remove( "django.contrib.staticfiles")

INSTALLED_APPS = apps
middleware = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    #"django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if not DOCKER_MODE:
    middleware.insert(0, 'corsheaders.middleware.CorsMiddleware')

MIDDLEWARE = middleware

ROOT_URLCONF = "unpet_api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "unpet_api.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# Configura la base de datos
if LOCAL_DB:
    # Modo de desarrollo, utiliza SQLite por defecto
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    # Modo de producción, utiliza MySQL en Clever Cloud
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'bmb72wbdmjin8klxpert',
            'USER': 'uauvrvass9qcwgye',
            'PASSWORD':'Zx80kAeYM8J6lEiuh64W',
            'HOST': 'bmb72wbdmjin8klxpert-mysql.services.clever-cloud.com',
            'PORT': 3306,
        }
    }

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
if DEBUG:
    EMAIL_HOST_USER = 'unpet2023.robot@gmail.com'
    EMAIL_HOST_PASSWORD='porlosanimales2023'
    DEFAULT_FROM_EMAIL ='unpet2023.robot@gmail.com'
else:
        # Tu dirección de correo de "no reply"
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    # La contraseña de tu dirección de correo
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
    # Otra vez, tu dirección de correo de "no reply"
    DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "es-co"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

#STATIC_URL = "static/"

# DEBUG? ....

if not RENDER_MODE:
    # Tell Django to copy statics to the `staticfiles` directory
    # in your application directory on Render.
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

    # Turn on WhiteNoise storage backend that takes care of compressing static files
    # and creating unique names for each version so they can safely be cached forever.
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"




if RENDER_MODE:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    CSRF_COOKIE_SAMESITE = 'None'
    SESSION_COOKIE_SAMESITE = 'None'
    CSRF_COOKIE_HTTPONLY = False
    SESSION_COOKIE_HTTPONLY = False
else:
    CSRF_COOKIE_SAMESITE = 'Lax'
    SESSION_COOKIE_SAMESITE = 'Lax'
    CSRF_COOKIE_HTTPONLY = False
    SESSION_COOKIE_HTTPONLY = False

AUTH_USER_MODEL = "accounts.User"

AUTHENTICATION_BACKENDS = [
    "accounts.backends.AccountsBackend",
    "django.contrib.auth.backends.ModelBackend",
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication"
    ],
}
