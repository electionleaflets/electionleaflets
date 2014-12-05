from django.conf.urls import patterns, include, handler500, url
from django.conf import settings

from django.views.generic.simple import direct_to_template

from tags.views import view_tag
from tags.models import Tag

info_dict = {
    'queryset': Tag.objects.all(),
}


urlpatterns = patterns(
    '',
    url(r'^/$',      direct_to_template, {'template': 'tags/index.html'}, name='tags'),    
    url(r'^/(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_list', 
                                 dict(info_dict, template_name='tags/index.html'), name='tag'),    
    url(r'^/(?P<slug>[\w_\-\.]+)/$',  view_tag, name='tag'),          
)

