
import os

ADMINS = (
    ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

# DATABASES define in environment specific settings file

TIME_ZONE = 'Europe/London'

LANGUAGE_CODE = 'en-GB'

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')
MEDIA_URL = '/media/'

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
    'tags'
]

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'south',
    
    'pagination',
] + LEAFLET_APPS


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "templates"),
)


