from django.conf.urls.defaults import patterns, include, handler500, url
from django.conf import settings

from django.views.generic.simple import direct_to_template

from constituencies.views import view_constituency, view_constituencies

urlpatterns = patterns(
    '',
    url(r'^/$',      view_constituencies, name='constituencies'),    
    url(r'^/(?P<slug>[\w_\-\.]+)/$',  view_constituency, name='constituency'),              
)

