import os
from .local import *

# local db를 쓰는 경우 postgres 세팅 후 사용
# 임시로 로컬을 사용하며 추후 dockerize 예정
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ["LOCAL_DB_NAME"],
        'USER': os.environ["LOCAL_DB_USER"],
        'PASSWORD': os.environ["LOCAL_DB_PASSWORD"],
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
