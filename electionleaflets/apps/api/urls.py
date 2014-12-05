from django.conf.urls import patterns, include, handler500, url
from django.conf import settings

from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_detail

from api import views

urlpatterns = patterns(
    '',
    url(r'^/$', direct_to_template, {'template': 'api/index.html'}, name='api_index'),                
    url(r'latest.(?P<format>(xml|json))$', views.latest,name='api_latest'),                

)

