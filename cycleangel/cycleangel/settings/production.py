from .base import *

import os

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cycleangel',
    }
}

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()
    

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
		    'compressor.filters.css_default.CssAbsoluteFilter',
		    'compressor.filters.cssmin.CSSMinFilter',
			]
COMPRESS_CSS_HASHING_METHOD = 'content'

WHITENOISE_GZIP_EXCLUDE_EXTENSIONS = ('png',)
DEBUG=False
