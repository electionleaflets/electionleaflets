from django.template  import RequestContext
from django.shortcuts import render_to_response, get_object_or_404


def view_full_image(request, image_key):
    from leaflets.models import LeafletImage
    
    li = get_object_or_404(LeafletImage, image_key=image_key)
    
    return render_to_response('leaflets/full.html', 
                            {
                                'image_key': image_key,
                                'leaflet': li.leaflet,
                            },
                            context_instance=RequestContext(request), )
