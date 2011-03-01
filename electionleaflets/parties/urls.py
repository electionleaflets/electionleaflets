from django.conf.urls.defaults import patterns, include, handler500, url
from django.conf import settings

from django.views.generic.simple import direct_to_template

from parties.views import view_party, view_attacking_party

urlpatterns = patterns(
    '',
    url(r'^/$',      direct_to_template, {'template': 'parties/index.html'}, name='parties'),    
    url(r'^/(?P<slug>[\w_\-\.]+)/$',  view_party,name='party'),          
    url(r'^/(?P<slug>[\w_\-\.]+)/attacking/$',  view_attacking_party,name='attacking_party'),              
)

