from global_settings import *


DEBUG=True
TEMPLATE_DEBUG=DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'electionleaflets.db',
        'USER': '',
        'PASSWORD': '',        
        'HOST': '',                
        'PORT': '',                        
    }
}
