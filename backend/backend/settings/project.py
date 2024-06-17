import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')
SECRET_KEY = 'django-insecure-$0o!#5g5a$xua=j@8a9&h+$#f%6_bok5i9)6inc6o5-*f2*pny'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'ATOMIC_REQUESTS': True,
    }
}
