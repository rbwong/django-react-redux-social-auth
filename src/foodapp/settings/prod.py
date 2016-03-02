from foodapp.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

PAGE_CACHE_SECONDS = 60

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(SITE_ROOT, 'db.sqlite'),
    }
}