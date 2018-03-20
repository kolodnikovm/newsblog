DATABASES = {
    'default': {
        'ENGINE': 'ENGINE',
        'NAME': 'NAME',
        'HOST': 'HOST',
        'USER': 'USER',
        'PASSWORD': 'PASSWORD',
        'PORT': 'PORT'
    }
}

MEDIA_URL = 'MEDIA/URL'
AUTH_USER_MODEL = 'AUTH_MODEL'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}
