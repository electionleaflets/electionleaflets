from django.conf.urls.defaults import patterns, include, handler500, url
from django.conf import settings

from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_detail

from leaflets.models import Leaflet

from leaflets.views import view_full_image, latest_leaflets

info_dict = {
    'queryset': Leaflet.objects.all(),
}

urlpatterns = patterns(
    '',
    url(r'^/$',      latest_leaflets, name='leaflets'),    
    url(r'^/add/$',  direct_to_template, {'template': 'leaflets/add.html'}, name='add_leaflet'),      
    url(r'^/full/(?P<image_key>\w+)/$',  view_full_image, name='full_image'),          
    url(r'^/(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', 
                                 dict(info_dict, template_name='leaflets/leaflet.html'), name='leaflet'),    
)

