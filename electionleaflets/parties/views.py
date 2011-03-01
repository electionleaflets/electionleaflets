from django.template  import RequestContext
from django.shortcuts import render_to_response, get_object_or_404


def view_party(request, slug):
    from parties.models import Party
    from leaflets.models import Leaflet
    import math
        
    party = get_object_or_404(Party, slug=slug)
    
    qs = Leaflet.objects.filter(publisher_party=party)
    
    total = qs.count()
    
    currentPage = request.GET.get('page', 1)
    totalPages = int(math.ceil(float(total)/12))
    
    
    return render_to_response('parties/party.html', 
                            {
                                'party': party,
                                'qs': qs,
                                'total': total,
                                'currentPage': currentPage,
                                'totalPages': totalPages,
                                'request': request,
                            },
                            context_instance=RequestContext(request) )
                            
def view_attacking_party(request, slug):
    from parties.models import Party
    from leaflets.models import Leaflet
    import math
        
    party = get_object_or_404(Party, slug=slug)
    
    qs = Leaflet.objects.filter(attacks__id=party.id)
    
    total = qs.count()
    
    currentPage = request.GET.get('page', 1)
    totalPages = int(math.ceil(float(total)/12))
    
    
    return render_to_response('parties/attacking_party.html', 
                            {
                                'party': party,
                                'qs': qs,
                                'total': total,
                                'currentPage': currentPage,
                                'totalPages': totalPages,
                                'request': request,
                            },
                            context_instance=RequestContext(request) )                            