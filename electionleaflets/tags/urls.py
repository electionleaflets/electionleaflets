from django.conf.urls.defaults import patterns, include, handler500, url
from django.conf import settings

from django.views.generic.simple import direct_to_template

from tags.views import view_tag

urlpatterns = patterns(
    '',
    url(r'^/$',      direct_to_template, {'template': 'tags/index.html'}, name='tags'),    
    url(r'^/(?P<slug>[\w_\-\.]+)/$',  view_tag, name='tag'),          
)

