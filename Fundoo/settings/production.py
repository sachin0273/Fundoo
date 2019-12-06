from .base import *
from .development import *
DEBUG = False

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DATABASE'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('PASSWORD'),
        'HOST': 'localhost',
        'PORT': '3306',
        'TEST': {
            'NAME': 'test_myproject',
        },
    }
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
