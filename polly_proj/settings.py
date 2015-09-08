import os

PROJ_NAME = 'polly_proj'
SITE_ID = 1
SECRET_KEY = 'vj@a2g&1odcihcu)6gz2ebr$vsfa)680d5ak)jj+-f&gu87m%g'
DEBUG = True
ALLOWED_HOSTS = []
ROOT_URLCONF = PROJ_NAME + '.urls'
WSGI_APPLICATION = PROJ_NAME + '.wsgi.application'
LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Europe/Kiev'
USE_I18N = True
USE_L10N = False
USE_TZ = True
STATIC_URL = '/static/'
CMS_PERMISSION = False
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, PROJ_NAME, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATES = [{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [
			os.path.join(BASE_DIR, PROJ_NAME, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': True,
            'context_processors': (
                    'django.contrib.auth.context_processors.auth',
                    'django.template.context_processors.debug',
                    'django.template.context_processors.i18n',
                    'django.template.context_processors.media',
                    'django.template.context_processors.static',
                    'django.template.context_processors.tz',
                    'django.template.context_processors.csrf',
                    'django.template.context_processors.request',
                    'django.contrib.messages.context_processors.messages',
                    'sekizai.context_processors.sekizai',
                    'cms.context_processors.cms_settings',
                )
        }
    },
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
)

INSTALLED_APPS = (
    'djangocms_admin_style',
    'djangocms_text_ckeditor',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_style',
    'djangocms_column',
    'djangocms_file',
    'djangocms_flash',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_teaser',
    'djangocms_video',
    'reversion',

    'bootstrapform',

    'polly_proj',
    'pawnshop',
)

LANGUAGES = (
    ('ru', 'ru'),
)

CMS_LANGUAGES = {
    1: [
        {
            'redirect_on_fallback': True,
            'public': True,
            'code': 'ru',
            'name': 'ru',
            'hide_untranslated': False,
        },
    ],
    'default': {
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
}

CMS_TEMPLATES = (
    ('fullwidth.html', 'Fullwidth'),
    ('sidebar_left.html', 'Sidebar Left'),
    ('sidebar_right.html', 'Sidebar Right')
)

CMS_PLACEHOLDER_CONF = {}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': 'project.db',
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    }
}

MIGRATION_MODULES = {
    'djangocms_flash': 'djangocms_flash.migrations_django',
    'djangocms_teaser': 'djangocms_teaser.migrations_django',
    'djangocms_inherit': 'djangocms_inherit.migrations_django',
    'djangocms_video': 'djangocms_video.migrations_django',
    'djangocms_column': 'djangocms_column.migrations_django',
    'djangocms_googlemap': 'djangocms_googlemap.migrations_django',
    'djangocms_picture': 'djangocms_picture.migrations_django',
    'djangocms_link': 'djangocms_link.migrations_django',
    'djangocms_file': 'djangocms_file.migrations_django',
    'djangocms_style': 'djangocms_style.migrations_django'
}

from .log_settings import *

