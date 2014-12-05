from django.conf.urls import patterns, include, handler500, url
from django.conf import settings

from django.views.generic.simple import direct_to_template

urlpatterns = patterns(
    '',
    url(r'^/$',      direct_to_template, {'template': 'analysis/index.html'}, name='analysis'),    
)

