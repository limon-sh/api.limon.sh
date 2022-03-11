import os
from datetime import timedelta
from glob import glob


ROOT_URLCONF = 'api.urls'

AUTH_USER_MODEL = 'user.User'

DEBUG = True

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'change_me')

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOST', ['*'])

HOST = os.environ.get('HOST', 'http://localhost:8000')

CORS_ORIGIN_ALLOW_ALL = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_DIR = 'static'
STATIC_URL = f'/{STATIC_DIR}/'
STATIC_ROOT = os.path.join(BASE_DIR, STATIC_DIR)

MEDIA_DIR = 'media'
MEDIA_URL = f'/{MEDIA_DIR}/'
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_DIR)

USE_TZ = True
TIME_ZONE = 'UTC'

DATE_FORMAT = '%Y-%m-%d'
TIME_FORMAT = '%H:%M:%S'
DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

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
    'apps.organization'
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

CONN_MAX_AGE = 60
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['POSTGRES_DB'],
        'HOST': os.environ['POSTGRES_HOST'],
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
        'USER': os.environ['POSTGRES_USER'],
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', '')
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
        'rest_framework_simplejwt.authentication.JWTAuthentication',
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

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://0.0.0.0:8002'
    }
}
