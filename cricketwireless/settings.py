"""
Django settings for cricketwireless project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False') != 'False'


ALLOWED_HOSTS = ['https://stark-river-42703.herokuapp.com/', 'www.yaaconnect.com', 'yaaconnect.com', '.yaaconnect.com']

# Redirect requests on http to https
SECURE_SSL_REDIRECT = not DEBUG

if DEBUG == True:
    ALLOWED_HOSTS = ALLOWED_HOSTS.append('localhost')


# ( Added for use with django-allauth package. )
AUTHENTICATION_BACKENDS = [
    # FROM ALLAUTH DOCS - "Needed to login by username in Django admin, regardless of `allauth`"
    'django.contrib.auth.backends.ModelBackend',

    # FROM ALLAUTH DOCS = "`allauth` specific authentication methods, such as login by e-mail"
    'allauth.account.auth_backends.AuthenticationBackend',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Allauth apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # -- Allows login to this application via Google
    'allauth.socialaccount.providers.google',

    # Custom apps
    'leads',

    # Other third party apps
    'crispy_forms',
    'tinymce',
    'phonenumber_field',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Third party package for simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    'whitenoise.middleware.WhiteNoiseMiddleware',

]

ROOT_URLCONF = 'cricketwireless.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['cricketwireless/templates'],
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

WSGI_APPLICATION = 'cricketwireless.wsgi.application'


# Database settings
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {

    # Development database. Automatically changed in production by django_heroku package.
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


# Strictly third party settings below.

import django_heroku

# -- Allauth additional settings

SITE_ID = 1

# ---- Provider specific settings

"""
NOTE: FROM ALLAUTH DOCS - You must set AUTH_PARAMS['access_type'] to offline in order to receive a refresh token
on first login and on reauthentication requests (which is needed to refresh authentication tokens in the 
background, without involving the user’s browser). When unspecified, Google defaults to online.
"""

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # FROM ALLAUTH DOCS - "For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:"
        'APP': {
            'client_id': os.environ.get('GOOGLE_OAUTH_CLIENT_ID', ''),
            'secret': os.environ.get('GOOGLE_OAUTH_CLIENT_SECRET', ''),
            'key': ''
        },
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

# ---- URL to redirect to on login.
LOGIN_REDIRECT_URL = '/employee'


# -- Prints emails to the console, only for use in development.
# -- Removes the need to run an SMTP server when developing on
# -- local machine.
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# -- Whitenoise settings

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# -- Heroku settings

# ---- Activate Django-Heroku.
django_heroku.settings(locals())


# -- Sentry production error reporting

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

if DEBUG == False:
    sentry_sdk.init(
        dsn="https://a60dd298dcdb409b9493b7dbfae824ae@o439053.ingest.sentry.io/5679994",
        integrations=[DjangoIntegration()],

        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0,

        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True
    )