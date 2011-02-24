from django.template  import RequestContext
from django.shortcuts import render_to_response, get_object_or_404


def view_tag(request, slug):
    from tags.models import Tag
    from leaflets.models import Leaflet
    from categories.models import Category
    
    tag = get_object_or_404(Tag, slug=slug)
    
    qs = Leaflet.objects.filter(tags__id=tag.id)
    
    return render_to_response('tags/tag.html', 
                            {
                                'tag': tag,
                                'qs': qs,
                                'total': qs.count(),
                                'request': request,
                                'categories': Category.objects.order_by('name').all(),
                            },
                            context_instance=RequestContext(request) )
