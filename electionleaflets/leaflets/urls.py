from django.conf.urls.defaults import patterns, include, handler500, url
from django.conf import settings

from django.views.generic.simple import direct_to_template


urlpatterns = patterns(
    '',
    url(r'^/$',      direct_to_template, {'template': 'leaflets/index.html'}, name='leaflets'),    
    url(r'^/add/$',  direct_to_template, {'template': 'leaflets/add.html'}, name='add_leaflet'),      
    url(r'^/(?P<leaflet_id>\d+)/$',  direct_to_template, {'template': 'leaflets/leaflet.html'}, name='leaflet'),          
)

