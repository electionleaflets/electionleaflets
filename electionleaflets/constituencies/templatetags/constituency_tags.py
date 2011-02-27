from django import template
from django.conf import settings
from leaflets.models import Leaflet

register = template.Library()

@register.inclusion_tag('constituencies/ordered_list.html')
def constituency_list_by_count():
    constituencies = []
    constituencies.append( {'slug': 'islington-south-and-finsbury', 'name': 'Islington South and Finsbury', 'count': 204} )
    constituencies.append( {'slug': 'oxford-east', 'name': 'Oxford East', 'count': 177} )
    
    return { 'MEDIA_URL': settings.MEDIA_URL, 'constituencies': constituencies }
    
@register.inclusion_tag('constituencies/zero_entry_list.html')
def constituency_list_with_none():
    constituencies = []
    constituencies.append( {'slug': 'islington-south-and-finsbury', 'name': 'Islington South and Finsbury'} )
    constituencies.append( {'slug': 'oxford-east', 'name': 'Oxford East'} )
    
    return { 'MEDIA_URL': settings.MEDIA_URL, 'constituencies': constituencies }    