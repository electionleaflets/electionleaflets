
from django.conf.urls.defaults import patterns, include, handler500, url
from django.conf import settings
from django.contrib import admin

from django.views.generic.simple import direct_to_template

admin.autodiscover()

handler500 # Pyflakes

urlpatterns = patterns(
    '',
    url(r'^$',      direct_to_template, {'template': 'core/home.html'}, name='home'),    
    url(r'^leaflets',   include('leaflets.urls')),        
    # Administration URLS
    (r'^admin/(.*)', admin.site.root),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
