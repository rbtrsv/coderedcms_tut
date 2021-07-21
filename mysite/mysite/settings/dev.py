from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '68ruz2&^5ioq-qp_f5f)+-140(%rdg=udva))i0!2*nwctr1t('

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += ['django_sass',]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

WAGTAIL_CACHE = False

try:
    from .local_settings import *
except ImportError:
    pass
