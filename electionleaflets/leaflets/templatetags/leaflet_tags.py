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