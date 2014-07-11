from settings import *
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'HOHDB1',
        'USER': 'postgres',
        'PASSWORD': 'ajit',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        #'ATOMIC_REQUESTS': True
    }
}
