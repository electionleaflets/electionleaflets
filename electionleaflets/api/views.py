from django.template  import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.sites.models import Site
from django.utils.html import escape

def latest(request, format):
    # TODO: Fix this to work properly
    from leaflets.models import Leaflet
        
    domain = Site.objects.get_current().domain
    
    leaflets = Leaflet.objects.order_by('-id').all()[0:20]
    resp = []
    for leaflet in leaflets:
        d = {}
        d['constituency'] = leaflet.get_first_constituency() or 'Unknown'
        d['constituency'] = str(d['constituency'])
        d['uploaded_date'] = str(leaflet.date_uploaded)
        d['delivery_date'] = str(leaflet.date_delivered)
        d['title'] = escape(leaflet.title)
        d['description'] = escape(leaflet.description)
        d['party'] = escape( leaflet.publisher_party.name )
        i = leaflet.get_first_image()
        if not isinstance(i, dict):
            d['small_image'] = 'http://%s%s' % (domain, i.get_small(),)
            d['medium_image'] = 'http://%s%s' % (domain, i.get_medium(),)
        d['link'] = leaflet.get_absolute_url()
        resp.append( d )
        
    output = '<?xml version="1.0" ?>\n'
    output += "<leaflets>"
    for d in resp:
        output += "<leaflet>"        
        for k,v in d.iteritems():
            output += "<" + k + ">"
            output += v
            output += "</" + k + ">"            
        output += "</leaflet>"

    output += "</leaflets>"
    return HttpResponse(output, content_type='text/xml')