from django.template  import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

import uuid


def add_leaflet_upload(request):
    from leaflets.forms import LeafletFileUploadForm
    from leaflets.models import UploadSession
    
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

            return HttpResponseRedirect( reverse('add_leaflet_info', kwargs={'upload_session_key':session.key}) )
    
    return render_to_response('leaflets/add.html', 
                            {
                                'form': form,
                            },
                            context_instance=RequestContext(request), )
    
    
def add_leaflet_info(request, upload_session_key):
    from leaflets.models import UploadSession, LeafletConstituency
    from leaflets.forms  import LeafletInfoForm
    from parties.models import Party
    from constituencies.views import constituency_by_postcode    
    from constituencies.models import Constituency
    from datetime import datetime
    
    session = get_object_or_404(UploadSession, key=upload_session_key)      
    s3keys = session.s3keys.split(',')  
    
    form = LeafletInfoForm(request.POST or None)
    parties = Party.objects.order_by('name').all()
    
    if request.method == 'POST':
        if form.is_valid():
            #exclude = ('lat','lng','date_uploaded', 'date_delivered', 'constituencies')
            leaflet = form.save(commit=False)
            leaflet.lat = leaflet.lng = 0
            leaflet.date_uploaded = datetime.now()

            # Update the leaflet and then associate the images
            # TODO: Fix me here
            leaflet.date_delivered = datetime.now()
            leaflet.save()
            
            try:
                cons = constituency_by_postcode( form.cleaned_data['postcode'] )
                if cons is not None:
                    c = Constituency.objects.get(name=cons)
                    if not cons in leaflet.constituencies.all():
                        LeafletConstituency(leaflet=leaflet, constituency=c).save()
            except Exception as e:
                print e
                
            # TODO: Handle uploadsession and process/save files before marking the 
            # session as published
    
        
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
    
    li = get_object_or_404(LeafletImage, image_key=image_key)
    
    return render_to_response('leaflets/full.html', 
                            {
                                'image_key': image_key,
                                'leaflet': li.leaflet,
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
    