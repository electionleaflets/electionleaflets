from django.conf.urls.defaults import patterns, include, handler500, url
from django.conf import settings

from django.views.generic.simple import direct_to_template

urlpatterns = patterns(
    '',
    url(r'^/$',      direct_to_template, {'template': 'constituencies/index.html'}, name='constituencies'),    
    url(r'^/(?P<constituency_name>[\w_\-\.]+)/$',  direct_to_template, {'template': 'constituencies/constituency.html'}, name='constituency'),              
)

