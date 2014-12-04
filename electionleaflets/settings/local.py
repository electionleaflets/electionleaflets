DEBUG = True
template_DEBUG = DEBUG


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'electionleaflets',
        'USER': 'symroe',
    }
}