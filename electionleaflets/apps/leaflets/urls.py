from django.conf.urls import patterns, url

from leaflets.views import (ImageView, LatestLeaflets,
    view_all_full_images, LeafletView, LeafletUploadWizzard)

from .forms import  (FrontPageImageForm, BackPageImageForm,
    InsidePageImageForm, PostcodeForm)

named_form_list = [
    ('front', FrontPageImageForm),
    ('postcode', PostcodeForm),
    # ('back', BackPageImageForm),
    # ('inside', InsidePageImageForm),
]

upload_form_wizzard = LeafletUploadWizzard.as_view(named_form_list,
    url_name='upload_step', done_step_name='finished')

urlpatterns = patterns(
    '',

    url(r'/add/(?P<step>.+)/$', upload_form_wizzard, name='upload_step'),
    url(r'/add/', upload_form_wizzard, name='upload_leaflet'),

    url(r'^/full/(?P<image_key>.+)/$',  ImageView.as_view(), name='full_image'),
    url(r'^/full/(?P<leafletid>\d+)/$',  ImageView.as_view(), name='full_images'),

    url(r'^/(?P<pk>\d+)/$', LeafletView.as_view(), name='leaflet'),
    url(r'^/$',      LatestLeaflets.as_view(), name='leaflets'),

    # url(r'^/add/(?P<upload_session_key>.+)/$',  add_leaflet_info, name='add_leaflet_info'),
    # url(
    #     r'^/add/$',
    #     LeafletUploadWizzard.as_view(),
    #     name='add_leaflet'),

    # url(r'^/rotate/(?P<direction>(left|right))/(?P<image_key>.+)/$',  rotate_image, name='rotate_image'),

)

