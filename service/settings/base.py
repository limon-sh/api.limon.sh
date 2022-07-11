import os
from datetime import timedelta
from glob import glob
from urllib.parse import urljoin


# Base django settings
DEBUG = True
APPEND_SLASH = False

ROOT_URLCONF = 'api.urls'
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'change_me')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# l10n and i18n
USE_TZ = True
TIME_ZONE = 'UTC'
DATE_FORMAT = '%Y-%m-%d'
TIME_FORMAT = '%H:%M:%S'
DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

# Auth settings
AUTH_USER_MODEL = 'user.User'
BACKEND_HOST = os.environ.get('BACKEND_HOST', 'http://localhost:8000')
FRONTEND_HOST = os.environ.get('FRONTEND_HOST', 'http://localhost:8080')
GOOGLE_OAUTH2_CLIENT_ID = os.environ['GOOGLE_OAUTH2_CLIENT_ID']
GOOGLE_OAUTH2_CLIENT_SECRET = os.environ['GOOGLE_OAUTH2_CLIENT_SECRET']
FRONTEND_SIGN_IN_URL = urljoin(
    FRONTEND_HOST, os.environ.get('FRONTEND_SIGN_IN_PATH', '/sign-in')
)
FRONTEND_SIGN_UP_URL = urljoin(
    FRONTEND_HOST, os.environ.get('FRONTEND_SIGN_UP_PATH', '/sign-up')
)

# CORS settings
CORS_ORIGIN_ALLOW_ALL = True
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOST', '*').split(',')
CORS_ALLOWED_ORIGINS = [
    BACKEND_HOST,
    FRONTEND_HOST
]

REDIS_HOST = os.environ.get('REDIS_HOST', 'redis')
REDIS_PORT = os.environ.get('REDIS_PORT', '6379')

# Static files
STATIC_DIR = 'static'
STATIC_URL = f'/{STATIC_DIR}/'
STATIC_ROOT = os.path.join(BASE_DIR, STATIC_DIR)
MEDIA_DIR = 'media'
MEDIA_URL = f'/{MEDIA_DIR}/'
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_DIR)
UPLOAD_AVATARS_TO = 'images/logo/'
IMAGE_UPLOAD_MAX_SIZE = 5 * 1024 * 1024
DEFAULT_FILE_STORAGE = 'libs.storages.LocalMediaStorage'
ALLOWED_IMAGE_EXTENSIONS = (
    ".jpeg",
    ".jpg",
    ".png"
)

INSTALLED_APPS = [
    # Django apps
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',

    # Required apps
    'drf_yasg',
    'corsheaders',
    'rest_framework',
    'django_extensions',

    # Project apps
    'apps.user',
    'apps.organization',
    'apps.project',
    'apps.product',
    'apps.machine',
    'apps.cluster'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CONN_MAX_AGE = 60 * 5
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'api_limon_sh_db'),
        'HOST': os.environ.get('POSTGRES_HOST', 'postgresql'),
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
        'USER': os.environ.get('POSTGRES_USER', 'user'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'password')
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{REDIS_HOST}:{REDIS_PORT}'
    }
}

TEMPLATES = (
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': glob('apps/**/templates/', recursive=True),
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
)

REST_FRAMEWORK = {
    'DATE_FORMAT': DATE_FORMAT,
    'TIME_FORMAT': TIME_FORMAT,
    'DATETIME_FORMAT': DATETIME_FORMAT,
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTStatelessUserAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'}
]

SIMPLE_JWT = {
    'USER_ID_FIELD': 'uuid',
    'UPDATE_LAST_LOGIN': True,
    'ROTATE_REFRESH_TOKENS': True,
    'ACCESS_TOKEN_LIFETIME': timedelta(
        seconds=int(os.environ.get('ACCESS_TOKEN_LIFETIME', 86400))
    ),
    'REFRESH_TOKEN_LIFETIME': timedelta(
        seconds=int(os.environ.get('REFRESH_TOKEN_LIFETIME', 172800))
    )
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}
