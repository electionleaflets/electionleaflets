from django.conf.urls import patterns, include, handler500, url
from django.conf import settings

from django.views.generic.list_detail import object_detail

from leaflets.models import Leaflet

from leaflets.views import (view_full_image, latest_leaflets,
    add_leaflet_upload, add_leaflet_info, rotate_image, view_all_full_images)

info_dict = {
    'queryset': Leaflet.objects.all(),
}

urlpatterns = patterns(
    '',
    url(r'^/$',      latest_leaflets, name='leaflets'),

    url(r'^/add/(?P<upload_session_key>.+)/$',  add_leaflet_info, name='add_leaflet_info'),
    url(r'^/add/$',  add_leaflet_upload, name='add_leaflet'),

    url(r'^/rotate/(?P<direction>(left|right))/(?P<image_key>.+)/$',  rotate_image, name='rotate_image'),

    url(r'^/full/(?P<leafletid>\d+)/$',  view_all_full_images, name='full_images'),
    url(r'^/full/(?P<image_key>.+)/$',  view_full_image, name='full_image'),

    url(r'^/(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail',
                                 dict(info_dict, template_name='leaflets/leaflet.html'), name='leaflet'),
)

