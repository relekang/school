import sys
from project.settings import *

#CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

with open('/django-sites/db-pw/django', 'rb') as f:
    db_password = f.readline()
db_password = db_password.replace("\n","").strip()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'school',
        'USER': 'django',
        'PASSWORD': db_password,
        'HOST': '127.0.0.1',
        'PORT': ''
    }
}

LOG_PRINT_LEVEL = 1

#SESSION_COOKIE_SECURE = True

sys.stdout = sys.stderr
