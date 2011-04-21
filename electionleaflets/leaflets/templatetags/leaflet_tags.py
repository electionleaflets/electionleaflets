from django import template
from django.conf import settings
from leaflets.models import Leaflet
import os

register = template.Library()

@register.inclusion_tag('leaflets/carousel.html')
def leaflet_carousel():
    leaflets = Leaflet.objects.filter().order_by('-id')[0:20]
    return { 'MEDIA_URL': settings.MEDIA_URL, 'leaflets': leaflets }
    
@register.simple_tag
def get_medium_image_from_upload(file_path):
    path = os.path.join(settings.MEDIA_URL, file_path.name)
    path = path.replace('uploads/', 'uploads/medium/')
    return path
    
@register.filter
def truncatesmart(value, limit=80):
    """
    Truncates a string after a given number of chars keeping whole words.
    
    Usage:
        {{ string|truncatesmart }}
        {{ string|truncatesmart:50 }}
    """
    
    try:
        limit = int(limit)
    # invalid literal for int()
    except ValueError:
        # Fail silently.
        return value
    
    # Make sure it's unicode
    value = unicode(value)
    
    # Return the string itself if length is smaller or equal to the limit
    if len(value) <= limit:
        return value
    
    # Cut the string
    value = value[:limit]
    
    # Break into words and remove the last
    words = value.split(' ')[:-1]
    
    # Join the words and return
    return ' '.join(words) + '...'