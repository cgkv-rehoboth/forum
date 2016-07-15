import os

DEBUG = False

TEMPLATE_DEBUG = False

SECRET_KEY = "Cp0:qA[Hkx!aknq<G.9hXAm3n//3Z.80=0QTK,J)'Vu1(S}+-\#9][p_+EZCuMiZ"

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'cgkv',
    'USER': 'cgkv',
    'PASSWORD': '(VM^0llC]QL_s-x2QP*J_E&n}l2ZOomKPn;nqLT',
    'HOST': 'localhost',
    'PORT': '3306',
  }
}

ALLOWED_HOSTS = [
  'localhost',
  'rehobothkerkwoerden.nl',
  'www.rehobothkerkwoerden.nl',
  'www.cgkvwoerden.nl',
  'www.gkvwoerden.nl',
  'www.cgkwoerden.nl',
  '159.100.68.110'
]
CORS_ORIGIN_ALLOW_ALL = False

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.rehobothkerkwoerden.nl'
EMAIL_HOST_USER = 'website@rehobothkerkwoerden.nl'
EMAIL_HOST_PASSWORD = 'nDZ-6bx-VhM-JCa'

LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,
  'handlers': {
    'console': {
      'class': 'logging.StreamHandler',
    },
  },
  'loggers': {
    'django': {
      'handlers': ['console'],
      'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
    },
  },
}
