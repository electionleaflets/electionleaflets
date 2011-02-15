from django import template
from django.conf import settings
from leaflets.models import Leaflet

register = template.Library()

@register.inclusion_tag('parties/ordered_list.html')
def party_list_by_count():
    parties = []
    parties.append( {'slug': 'liberal_democrats', 'name': 'Liberal Democrats', 'count': 1522} )
    parties.append( {'slug': 'the_labour_party', 'name': 'The Labour party', 'count': 1359} )
    return { 'MEDIA_URL': settings.MEDIA_URL, 'parties': parties }