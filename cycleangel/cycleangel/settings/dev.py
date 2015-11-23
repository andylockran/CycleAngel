from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zfj2)*5j5482_f0qx03#ny-d&h2+$-vkza8p7=96n-7bl8^!&!'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
