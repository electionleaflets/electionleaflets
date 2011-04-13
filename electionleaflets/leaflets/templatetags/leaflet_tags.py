from django import template
from django.conf import settings
from leaflets.models import Leaflet

register = template.Library()

@register.inclusion_tag('leaflets/carousel.html')
def leaflet_carousel():
    leaflets = Leaflet.objects.filter().order_by('-id')[0:20]
    return { 'MEDIA_URL': settings.MEDIA_URL, 'leaflets': leaflets }