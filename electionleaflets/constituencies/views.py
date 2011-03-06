from django.template  import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse


def view_constituencies(request):
    """
    Provides a form to lookup constituencies either by name or by 
    postcode.
    """
    from constituencies.models import Constituency
    from constituencies.forms import ConstituencyLookupForm
    from leaflets.models import Leaflet
    
    constituencies = Constituency.objects.order_by('name').all()
    
    form = ConstituencyLookupForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            postcode = form.cleaned_data['search']
            if postcode:
                #TODO: Not yet implemented
                pass
            
            cons = form.cleaned_data['constituency']
            if cons:
                return HttpResponseRedirect(reverse('constituency', kwargs={'slug': cons.slug}) )

    
    return render_to_response('constituencies/index.html', 
                            {
                                'constituencies': constituencies,
                            },
                            context_instance=RequestContext(request) )


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
