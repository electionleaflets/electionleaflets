import logging
import uuid
import sys, os

from django.template  import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import DetailView

from .models import Leaflet



@staff_member_required
def rotate_image(request, direction, image_key):
    from PIL import Image
    from leaflets.models import UploadSession

    referer = request.META.get('HTTP_REFERER')
    if not referer:
        raise Http404()

    angle = {'left': 90, 'right': -90}
    p = os.path.join(settings.MEDIA_ROOT, 'uploads')
    p = os.path.join(p, image_key) + '.jpg'

    try:
        img = Image.open(p)
        img = img.rotate(angle[direction], expand=True)
        img.save(p, "JPEG")

        # HACKY
        u = UploadSession()
        u.resize_file( p, 'thumbnail', 140, 0 )
        u.resize_file( p, 'small', 120, 0 )
        u.resize_file( p, 'medium', 300, 0 )
        u.resize_file( p, 'large', 1024, 0 )
    except Exception, e:
       raise e
    return HttpResponseRedirect(referer)


def add_leaflet_upload(request):
    from leaflets.forms import LeafletFileUploadForm

    form = LeafletFileUploadForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            # Do thumbnail and upload files to make sure they make it to S3
            session = form.save(commit=False)

            # Create an upload session and add the keys to the session so we can find it
            # easily on the next page. Ideally the s3keys will contain the keys of the
            # files we have stored on S3 by now.
            session.key = str(uuid.uuid4())
            session.save()

            session.handle_file_uploads()

            return HttpResponseRedirect(
                reverse('add_leaflet_info',
                        kwargs={'upload_session_key':session.key}) )
        raise Exception(form.errors)
    return render_to_response('leaflets/add.html',
                            {
                                'form': form,
                            },
                            context_instance=RequestContext(request), )

def add_leaflet_info(request, upload_session_key):
    from leaflets.models import UploadSession, LeafletConstituency, LeafletTag, LeafletCategory, LeafletPartyAttack, LeafletImage
    from leaflets.forms  import LeafletInfoForm
    from parties.models import Party
    from tags.models import Tag
    from constituencies.views import constituency_by_postcode
    from constituencies.models import Constituency
    from datetime import datetime, timedelta
    from third_party.mapit import postcode_to_latlong
    from django.db.models import F

    session = get_object_or_404(UploadSession, key=upload_session_key)
    s3keys = session.s3keys.split(',')

    form = LeafletInfoForm(request.POST or None)
    parties = Party.objects.order_by('name').all()

    if request.method == 'POST':
        if form.is_valid():
            leaflet = form.save(commit=False)

            # This is obviously very UK specific, and I am a little loathe to go the whole zope style
            # provider/interface path, but ...
            # TODO: Provide hook for non-uk lookup for postcode/zipcode
            lat, lon = postcode_to_latlong(leaflet.postcode)
            leaflet.lat = lat or 0
            leaflet.lng =  lon or 0

            leaflet.date_uploaded = datetime.now()
            leaflet.date_delivered = datetime.now() - timedelta( int(form.cleaned_data['date_delivered_text']) )
            leaflet.live = 1
            leaflet.save()

            # Increment the count of leaflets
            Party.objects.filter(id=leaflet.publisher_party.id).update(count=F('count') + 1)

            for t in form.cleaned_data['tags'].split(','):
                obj, created = Tag.objects.get_or_create(tag=t,tag_clean=t)
                lt, created = LeafletTag.objects.get_or_create(leaflet=leaflet, tag=obj)

            source = request.session.get('source', None)
            if source:
                obj, created = Tag.objects.get_or_create(tag=source,tag_clean=source)
                lt, created = LeafletTag.objects.get_or_create(leaflet=leaflet, tag=obj)

            for c in form.cleaned_data['categories']:
                LeafletCategory.objects.get_or_create(leaflet=leaflet, category=c)

            for a in form.cleaned_data['attacks']:
                LeafletPartyAttack.objects.get_or_create(leaflet=leaflet, party=a)

            try:
                cons = constituency_by_postcode( form.cleaned_data['postcode'] )
                if cons is not None:
                    c = Constituency.objects.get(name=cons)
                    if not cons in leaflet.constituencies.all():
                        LeafletConstituency(leaflet=leaflet, constituency=c).save()
                        Constituency.objects.filter(id=c.id).update(count=F('count') + 1)
            except:
                logging.error( "Unexpected error:", sys.exc_info()[0])

            s = 1
            for name in session.names():
                LeafletImage.objects.get_or_create(image_key=name,leaflet=leaflet,sequence=s)
                s = s + 1

            return HttpResponseRedirect( reverse('leaflet',kwargs={'object_id': leaflet.id}))

    return render_to_response('leaflets/add_step2.html',
                            {
                                'form': form,
                                'session': session,
                                's3keys': s3keys, # For the images
                                'parties': parties,
                            },
                            context_instance=RequestContext(request), )




def view_full_image(request, image_key):
    from leaflets.models import LeafletImage

    li = LeafletImage.objects.filter(image_key=image_key)
    if li.count() == 1:
        li = get_object_or_404(LeafletImage, image_key=image_key)
    else:
        # Should not do this, we'll need to fix it - probably and upload artifact
        li = li.all()[0]

    return render_to_response('leaflets/full.html',
                            {
                                'image': li,
                                'leaflet': li.leaflet,
                            },
                            context_instance=RequestContext(request), )

def view_all_full_images(request, leafletid):
    from leaflets.models import Leaflet, LeafletImage

    leaflet = get_object_or_404(Leaflet, pk=leafletid)
    images = LeafletImage.objects.filter(leaflet=leaflet)

    return render_to_response('leaflets/full_all.html',
                            {
                                'images': images,
                                'leaflet': leaflet,
                            },
                            context_instance=RequestContext(request), )


def latest_leaflets( request ):
    import math
    from leaflets.models import Leaflet

    qs = Leaflet.objects.order_by('-id')
    total = qs.count()

    currentPage = request.GET.get('page', 1)
    totalPages = int(math.ceil(float(total)/12))

    return render_to_response('leaflets/index.html',
                            {
                                'qs': qs,
                                'total': total,
                                'request': request,
                                'currentPage': currentPage,
                                'totalPages': totalPages,
                            },
                            context_instance=RequestContext(request) )


class LeafletView(DetailView):
    template_name='leaflets/leaflet.html'
    queryset = Leaflet.objects.all()

