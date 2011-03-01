

def settings(request):
    """
    Add settings (or some) to the templates
    """
    from django.conf         import settings

    tags = {}            
    tags['GOOGLE_MAPS_KEY'] = settings.GOOGLE_MAPS_KEY
    
    return tags
