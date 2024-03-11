from .base import *

#Defining the email backend Configurations

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#"djcelery_email_backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_USE_TLS = True
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = "info@magni-homes.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Magni Homes"

DATABASES = {
    'default': {
        'ENGINE': env("POSTGRES_ENGINE"),
        'NAME': env("POSTGRES_DB"),
        'USER': env("POSTGRES_USER"),
        'PASSWORD': env("POSTGRES_PASSWORD"),
        'HOST': env("PG_HOST"),
        'PORT': env("PG_PORT"),
    }
}
#CELERY_BROKER_URL = env("CELERY_BROKER_URL")
#CELERY_RESULTS_BACKEND = env("CELERY_BACKEND")
#CELERY_TIMEZONE = env("CELERY_TIMEZONE")