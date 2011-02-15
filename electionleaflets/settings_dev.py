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
    },
    # Used for exporting the existing data from the original UK database.
    # This will eventually be removed.
    'export': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'leaflets_old',
        'USER': 'root',
        'PASSWORD': '',        
        'HOST': 'localhost',                
        'PORT': '',                        
    },
}
