# -*- coding: utf-8 -*-
"""
Django settings for running the example of spirit app
"""

from __future__ import unicode_literals

import os
import sys

from spirit.settings import *

# You may override or extend spirit settings below...

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

DEBUG = False

ADMINS = (('Arjen Rouvoet', 'a.j.rouvoet@gmail.com'), )

SECRET_KEY = "b@4qbf2tg=d*xxldk08_gauzg639x&53nxm*he&-#c9&4i&2o="

ALLOWED_HOSTS = ['localhost', '.rehobothkerkwoerden.nl', ]

DEFAULT_FROM_EMAIL = 'info@rehobothkerkwoerden.nl'  # Django default
SERVER_EMAIL = DEFAULT_FROM_EMAIL

# This will be the default in next version
ST_RATELIMIT_CACHE = 'st_rate_limit'

ROOT_URLCONF = 'forum.urls'

WSGI_APPLICATION = 'forum.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Send an email to the site admins
# on error when DEBUG=False,
# log to console on error always.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'django.log'),
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django': {
            'handlers': ['console', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'cgkv.forum.db',
  }
}

# These are all the languages Spirit provides.
gettext_noop = lambda s: s
LANGUAGES = [
    ('de', gettext_noop('German')),
    ('en', gettext_noop('English')),
    ('es', gettext_noop('Spanish')),
    ('fr', gettext_noop('French')),
    ('hu', gettext_noop('Hungarian')),
    ('pl', gettext_noop('Polish')),
    ('pl-pl', gettext_noop('Poland Polish')),
    ('ru', gettext_noop('Russian')),
    ('sv', gettext_noop('Swedish')),
    ('tr', gettext_noop('Turkish')),
    ('zh-hans', gettext_noop('Simplified Chinese')),
]

# Default language
LANGUAGE_CODE = 'en'

# Keep templates in memory
del TEMPLATES[0]['APP_DIRS']
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
]

# Append the MD5 hash of the file’s content to the filename
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

#
# localsettings loading
#

localsettingspath = os.path.join(BASE_DIR, "forum/localsettings.py")
if os.path.exists(localsettingspath):
    from forum.localsettings import *
