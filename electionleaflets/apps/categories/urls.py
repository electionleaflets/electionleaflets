from django.conf.urls.defaults import patterns, include, handler500, url
from django.conf import settings

from django.views.generic.simple import direct_to_template

from categories.views import view_category

urlpatterns = patterns(
    '',
    url(r'^/$',      direct_to_template, {'template': 'categories/index.html'}, name='categories'),    
    url(r'^/(?P<slug>[\w_\-\.]+)/$',  view_category, name='category'),          
)

