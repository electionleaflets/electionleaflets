from django.template  import RequestContext
from django.shortcuts import render_to_response, get_object_or_404


def view_category(request, slug):
    from categories.models import Category
    from leaflets.models import Leaflet
    
    category = get_object_or_404(Category, slug=slug)
    
    qs = Leaflet.objects.filter(categories__id=category.id)
    
    return render_to_response('categories/category.html', 
                            {
                                'category': category,
                                'qs': qs,
                                'total': qs.count(),
                                'request': request
                            },
                            context_instance=RequestContext(request) )
