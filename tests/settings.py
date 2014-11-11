from __future__ import unicode_literals

import os

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',

    'django_ace',

    # The templates library
    'tablets',

    # Houses some basic stuff
    'core',
]

######## TEMPLATES CONFIG
TEMPLATE_LOADERS = (
    'django_jinja.loaders.AppLoader',  # Optional, only needed if you also have .jinja file templates
    'django_jinja.loaders.FileSystemLoader',  # Optional, only needed if you also have .jinja file templates
    # 'django.template.loaders.filesystem.Loader', # Optional -- Not needed if you have the above jinja template loaders, as they encompass this logic
    # 'django.template.loaders.app_directories.Loader', # Optional -- Not needed if you have the above jinja template loaders, as they encompass this logic
    'tablets.loaders.DatabaseLoader',
)
JINJA2_TEMPLATE_CLASS = "django_jinja.base.Template"
JINJA2_LOADER = "tablets.j2.loaders.Jinja2DatabaseOrFileLoader"

TEMPLATE_DIRS = (
    'templates',
)
######## END TEMPLATES CONFIG


TEST_RUNNER = "django.test.runner.DiscoverRunner"

SITE_ID = 1

ROOT_URLCONF = "urls"

DEBUG = True

STATIC_URL = '/static/'

SECRET_KEY = 'whatever man these are tests'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(__file__), 'database.db'),
    }
}