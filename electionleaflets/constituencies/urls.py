from django.conf.urls.defaults import patterns, include, handler500, url
from django.conf import settings

from django.views.generic.simple import direct_to_template

from constituencies.views import view_constituency, view_constituencies, view_not_spots

urlpatterns = patterns(
    '',
    url(r'^/$',      view_constituencies, name='constituencies'),    
    url(r'^/notspots/', view_not_spots, name='constituency_notspots'),                  
    url(r'^/(?P<slug>[\w_\-\.]+)/$',  view_constituency, name='constituency'),              
)

