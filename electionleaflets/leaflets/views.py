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
    