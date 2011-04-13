from django.conf.urls.defaults import patterns, include, handler500, url
from django.conf import settings

from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_detail


urlpatterns = patterns(
    '',
    url(r'^/$', direct_to_template, {'template': 'api/index.html'}, name='api_index'),                

)

