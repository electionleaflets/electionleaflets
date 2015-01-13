DEBUG = True
template_DEBUG = DEBUG

THUMBNAIL_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'electionleaflets',
        'USER': 'symroe',
    }
}