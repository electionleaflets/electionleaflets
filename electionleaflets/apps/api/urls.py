from django.conf.urls import patterns, include, handler500, url
from django.conf import settings
from django.views.generic import TemplateView

from api import views

urlpatterns = patterns(
    '',
    url(r'^/$', TemplateView.as_view(template_name='api/index.html'), name='api_index'),
    url(r'latest.(?P<format>(xml|json))$', views.latest,name='api_latest'),

)

