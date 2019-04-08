from .base import *

DEBUG = True

INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

INTERNAL_IPS = ['127.0.0.1', ]

# local db를 쓰는 경우 postgres 세팅 후 사용
# dockerize 예정
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.environ["LOCAL_DB_NAME"],
#         'USER': os.environ["LOCAL_DB_USER"],
#         'PASSWORD': os.environ["LOCAL_DB_PASSWORD"],
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
