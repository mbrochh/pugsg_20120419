import os

from pugsg20120419.settings import *  # NOQA


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}


COVERAGE_MODULE_EXCLUDES = [
    r'log$',
    r'fixtures',
    r'templates',
    r'locale',
    r'media',
    r'modifiers',
    r'search_indexes',
    r'migrations',
    r'static',
]
