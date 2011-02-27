from django.conf.urls.defaults import patterns, include, handler500, url
from django.conf import settings

from django.views.generic.simple import direct_to_template

from parties.views import view_party

urlpatterns = patterns(
    '',
    url(r'^/$',      direct_to_template, {'template': 'parties/index.html'}, name='parties'),    
    url(r'^/(?P<slug>[\w_\-\.]+)/$',  view_party,name='party'),          
)

