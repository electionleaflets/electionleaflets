from django import template
from django.conf import settings

register = template.Library()

@register.inclusion_tag('leaflets/carousel.html')
def leaflet_carousel():
    # TODO: Retrieve the X latest leaflets and send them to the carousel page
    # Until we have data let's cheat
    
    leaflets = []
    leaflets.append( {'id': 6237, 'uuid': '78d97155cc3b63cad21b1aeb904c08a3' } )
    leaflets.append( {'id': 6236, 'uuid': '63d2519d479a64c34520bd5f16f5b118' } )    
    
    return { 'MEDIA_URL': settings.MEDIA_URL, 'leaflets': leaflets }