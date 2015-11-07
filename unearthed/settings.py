"""
Django settings for unearthed project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*)lv=fh_&7p0fgo6j-pb^f_t_8-llz@oq-4&-lc!#6tp&)y-1t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'helian',
    'djangobower',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

# STATICFILES_FINDERS = (
#     'djangobower.finders.BowerFinder',
# )

ROOT_URLCONF = 'unearthed.urls'


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

WSGI_APPLICATION = 'unearthed.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = (
                    os.path.join(BASE_DIR, "static"),
                    )
# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
# STATICFILES_DIRS = (
#     "C:/djangoprojects/unearthed/static",
#     )
STATIC_URL = '/static/'

BOWER_COMPONENTS_ROOT = '/bower_components/'

BOWER_INSTALLED_APPS = ('mocha#1.17.1',
 'datatables-plugins#1.0.1',
 'metisMenu#1.1.3',
 'raphael#2.1.4',
 'morrisjs#0.5.1',
 'flot#0.8.3',
 'datatables-responsive#1.0.7',
 'flot.tooltip#0.8.5',
 'bootstrap-social#4.8.0',
 'bootstrap#3.3.5',
 'morris.js#0.5.1',
 'startbootstrap-sb-admin-2#1.0.7',
 'font-awesome#4.2.0',
 'holderjs#2.4.1',
 'jquery#2.1.4',
 'datatables#1.10.9')
