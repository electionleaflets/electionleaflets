from django.template  import RequestContext
from django.shortcuts import render_to_response, get_object_or_404


def view_constituency(request, slug):
    from constituencies.models import Constituency
    from leaflets.models import Leaflet
    import math
    
    const = get_object_or_404(Constituency, slug=slug)
    
    qs = Leaflet.objects.filter(constituencies__id=const.id)
    
    total = qs.count()
    currentPage = request.GET.get('page', 1)
    totalPages = int(math.ceil(float(total)/12))
    
    
    return render_to_response('constituencies/constituency.html', 
                            {
                                'constituency': const,
                                'qs': qs,
                                'total': total,
                                'currentPage': currentPage,
                                'totalPages': totalPages,
                                'request': request
                            },
                            context_instance=RequestContext(request) )
