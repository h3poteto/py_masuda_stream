"""
Django settings for masuda_stream project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

DJANGO_ENV = os.getenv('DJANGO_ENV', 'dev')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', '+dkhq_prp(9g_twakp*8!07e*l(jin6y!d$x6!p0ghbpsf_*h5')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if DJANGO_ENV == 'prod' else True

CSRF_COOKIE_SECURE = True if DJANGO_ENV == 'prod' else False

SESSION_COOKIE_SECURE = True if DJANGO_ENV == 'prod' else False

ALLOWED_HOSTS = [
    '*',
] if DJANGO_ENV == 'prod' else []


# Application definition

INSTALLED_APPS = [
    'frontend.apps.FrontendConfig',
    'masuda.apps.MasudaConfig',
    'user.apps.UserConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_extensions',
    'webpack_loader',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth_hatena',
    'django_slack',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'masuda_stream.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'allauth', 'templates')],
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

WSGI_APPLICATION = 'masuda_stream.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'masuda_stream',
        'HOST': os.getenv('DB_HOST', 'mysql'),
        'USER': os.getenv('DB_USER', 'root'),
        'PORT': os.getenv('DB_PORT', '3306'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'CONN_MAX_AGE': 20,
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
        'TEST': {
            'NAME': 'masuda_stream_test',
            'CHARSET': 'utf8mb4',
            'COLLATION': 'utf8mb4_general_ci',
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'ja-jp'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

# Using django-webpack-loader
# https://github.com/ezhome/django-webpack-loader
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'public'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')


WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'assets/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'formatters': {  # formatter attributes: https://docs.python.org/3/library/logging.html#logrecord-attributes
        'debug': {
            'format': '\t'.join([
                "[%(levelname)s]",
                "message:%(message)s",
                "asctime:%(asctime)s",
                "module:%(module)s",
                "process:%(process)d",
                "thread:%(thread)d",
            ])
        },
        'json': {  # using python-json-logger
            'format': '%(message)s %(lineno)d %(pathname)s',
            'class': 'pythonjsonlogger.jsonlogger.JsonFormatter',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'json' if DJANGO_ENV == 'prod' else 'debug',
        },
        'slack': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],  # remove this line if you test in development.
            'class': 'django_slack.log.SlackExceptionHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'slack'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1

# https://github.com/h3poteto/django-allauth/blob/master/allauth/socialaccount/providers/oauth/views.py#L47
# ここでscopeをスペース区切りにしているが
# hatena側では%2C = ,にしろといっている
# http://developer.hatena.ne.jp/ja/documents/auth/apis/oauth/consumer
# そのため複数指定をカンマ区切りに強制している
SOCIALACCOUNT_PROVIDERS = {
    'hatena': {
      'SCOPE': ['read_public,write_public']
    }
}

LOGIN_REDIRECT_URL = "/"

SLACK_TOKEN = os.getenv('SLACK_TOKEN')
SLACK_CHANNEL = os.getenv('SLACK_CHANNEL', '#playground')
SLACK_USERNAME = "masuda-stream"
SLACK_FAIL_SILENTLY = True
# TODO: use celery backend in production
SLACK_BACKEND = 'django_slack.backends.UrllibBackend'


LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
