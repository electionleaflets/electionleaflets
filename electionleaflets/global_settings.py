import os

# DATABASES define in environment specific settings file

TIME_ZONE = 'Europe/London'

LANGUAGE_CODE = 'en-GB'

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')
MEDIA_URL = '/media/'

SITE_ID=1

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin_media/'

# Don't share this with anybody.
SECRET_KEY = 'ik%cd@pu-lb@-r%($o4&p0+mcr16f3jij)g83pae@sl8v&g*-k'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'electionleaflets.urls'


LEAFLET_APPS = [
    'core',
    'leaflets',
    'parties',
    'constituencies',
    'analysis',
    'categories',
    'tags',
    'boundaries',
    'content',
    # Temporarily removing elections code
    #'elections',
]

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'south',
    'pagination',
    'crispy_forms',
] + LEAFLET_APPS

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
    'django.core.context_processors.debug',
    'core.context_processors.settings',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "templates"),
)


