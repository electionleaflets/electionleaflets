

def settings(request):
    """
    Add settings (or some) to the templates
    """
    from django.conf         import settings

    tags = {}            
    tags['GOOGLE_MAPS_KEY'] = settings.GOOGLE_MAPS_KEY
    if hasattr(settings, 'GOOGLE_ANALYTICS_KEY'):
        tags['GOOGLE_ANALYTICS_KEY'] = settings.GOOGLE_ANALYTICS_KEY
    return tags
