from .base import *
from .production import *
DEBUG = True

INSTALLED_APPS += [
    'django_extensions',
    'rest_framework',
    'django.contrib.sites',
    'rest_framework_swagger',
    'rest_framework.authtoken',
    'users',
    'Note',
    'django_elasticsearch_dsl',
    'django_nose',
    'corsheaders',
    'urlshortening',
    'storages',
    'django_social_share',
    'social_django'
]

MIDDLEWARE += ['corsheaders.middleware.CorsMiddleware',
               'django.middleware.common.BrokenLinkEmailsMiddleware',
               'django.middleware.common.CommonMiddleware',
               'Fundoo.middleware.login_required_middleware',
               'Fundoo.middleware.LabelCollaborators', ]

CORS_ORIGIN_ALLOW_ALL = True

REST_FRAMEWORK = {'DEFAULT_AUTHENTICATION_CLASSES': [
    'rest_framework_simplejwt.authentication.JWTAuthentication',
    'rest_framework.authentication.TokenAuthentication',
],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'localhost:9200'
    },
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    },
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {pathname} {lineno} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.FileHandler',
            'filename': 'Fundoo/mylog.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'Note': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': True,
        },
        'users.views': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': True,
        },

    }
}

