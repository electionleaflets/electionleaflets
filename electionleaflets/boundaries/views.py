from PIL import Image, ImageDraw
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.db.models import Q
from boundaries.models import Boundary
from parties.models import Party
from leaflets.models import Leaflet
from django.http import HttpResponse
import math
import random
google_dist = 20037508.34

def boundry_json(request):
  return HttpResponse('{ "type": "Polygon", "coordinates": [ [ [ -0.105987, 51.422577 ], [ -0.109374, 51.423158 ], [ -0.113192, 51.423270 ], [ -0.114605, 51.423467 ], [ -0.114031, 51.425160 ], [ -0.113999, 51.425657 ], [ -0.114602, 51.427500 ], [ -0.114331, 51.430032 ], [ -0.114425, 51.430925 ], [ -0.114557, 51.431182 ], [ -0.115803, 51.432174 ], [ -0.116697, 51.432672 ], [ -0.117852, 51.433060 ], [ -0.117468, 51.433425 ], [ -0.118064, 51.433943 ], [ -0.117953, 51.434159 ], [ -0.117152, 51.434564 ], [ -0.113184, 51.436105 ], [ -0.111220, 51.437085 ], [ -0.107892, 51.437845 ], [ -0.106031, 51.438984 ], [ -0.106203, 51.439424 ], [ -0.106197, 51.440191 ], [ -0.108746, 51.440419 ], [ -0.108618, 51.441008 ], [ -0.108273, 51.441512 ], [ -0.109285, 51.442267 ], [ -0.111519, 51.444844 ], [ -0.109744, 51.445250 ], [ -0.110364, 51.446011 ], [ -0.110856, 51.447246 ], [ -0.111570, 51.448310 ], [ -0.111641, 51.448941 ], [ -0.111135, 51.449893 ], [ -0.111195, 51.450241 ], [ -0.112162, 51.451272 ], [ -0.112403, 51.451730 ], [ -0.112410, 51.452378 ], [ -0.111185, 51.452473 ], [ -0.110944, 51.452663 ], [ -0.111159, 51.453643 ], [ -0.111813, 51.454871 ], [ -0.111668, 51.454903 ], [ -0.111876, 51.455368 ], [ -0.113735, 51.455207 ], [ -0.115730, 51.460763 ], [ -0.115717, 51.461197 ], [ -0.115381, 51.462021 ], [ -0.112505, 51.468321 ], [ -0.112543, 51.470436 ], [ -0.109072, 51.470795 ], [ -0.106772, 51.470509 ], [ -0.105040, 51.470575 ], [ -0.101540, 51.470275 ], [ -0.100773, 51.471340 ], [ -0.099397, 51.472627 ], [ -0.098917, 51.471934 ], [ -0.095997, 51.469881 ], [ -0.094106, 51.470741 ], [ -0.093663, 51.471718 ], [ -0.093080, 51.472127 ], [ -0.092718, 51.469774 ], [ -0.090071, 51.466087 ], [ -0.090667, 51.463294 ], [ -0.092212, 51.461121 ], [ -0.091776, 51.460047 ], [ -0.089940, 51.458408 ], [ -0.090015, 51.457677 ], [ -0.090735, 51.456430 ], [ -0.090691, 51.456060 ], [ -0.089407, 51.454614 ], [ -0.088506, 51.454105 ], [ -0.086931, 51.455118 ], [ -0.083783, 51.457664 ], [ -0.080227, 51.461773 ], [ -0.079534, 51.461396 ], [ -0.078569, 51.461456 ], [ -0.077210, 51.461810 ], [ -0.076378, 51.461527 ], [ -0.075255, 51.460722 ], [ -0.071421, 51.461417 ], [ -0.071161, 51.457427 ], [ -0.067761, 51.457064 ], [ -0.065807, 51.456214 ], [ -0.067660, 51.453685 ], [ -0.066171, 51.452713 ], [ -0.064785, 51.451557 ], [ -0.066977, 51.450232 ], [ -0.068096, 51.448715 ], [ -0.067419, 51.448490 ], [ -0.067076, 51.448774 ], [ -0.066522, 51.448607 ], [ -0.065874, 51.449049 ], [ -0.065524, 51.448884 ], [ -0.065322, 51.449082 ], [ -0.065407, 51.449161 ], [ -0.063931, 51.449742 ], [ -0.063800, 51.449574 ], [ -0.063315, 51.449644 ], [ -0.063307, 51.448603 ], [ -0.063788, 51.447847 ], [ -0.062220, 51.447352 ], [ -0.063084, 51.446184 ], [ -0.063640, 51.444809 ], [ -0.063666, 51.443355 ], [ -0.063870, 51.442526 ], [ -0.064219, 51.441909 ], [ -0.065026, 51.441157 ], [ -0.064054, 51.440849 ], [ -0.063701, 51.437930 ], [ -0.063457, 51.437541 ], [ -0.064420, 51.437041 ], [ -0.065834, 51.434631 ], [ -0.066709, 51.433923 ], [ -0.069622, 51.432657 ], [ -0.070695, 51.432458 ], [ -0.072383, 51.432412 ], [ -0.073586, 51.431352 ], [ -0.074894, 51.429749 ], [ -0.075093, 51.428796 ], [ -0.074327, 51.427449 ], [ -0.073936, 51.426153 ], [ -0.074996, 51.425660 ], [ -0.078336, 51.420564 ], [ -0.078549, 51.419848 ], [ -0.080092, 51.419672 ], [ -0.082346, 51.419772 ], [ -0.085539, 51.419289 ], [ -0.086426, 51.419306 ], [ -0.088190, 51.419927 ], [ -0.089584, 51.420960 ], [ -0.091395, 51.421723 ], [ -0.092308, 51.422354 ], [ -0.093919, 51.422798 ], [ -0.098108, 51.422574 ], [ -0.105987, 51.422577 ] ] ] }', mimetype="application/json")

def leaflet_polygon_options(boundary):
    n = Leaflet.objects.filter(leafletconstituency__constituency__boundary = boundary).count()
    return {"fill": leaflet_colour(n), "outline": (0,0,0,170)}

def leaflet_popup(boundary):
    party_list = [(p,
                   Leaflet.objects.filter(leafletconstituency__constituency__boundary = boundary,
                                          publisher_party = p))
                  for p
                  in Party.objects.filter(leaflet__leafletconstituency__constituency__boundary = boundary).distinct().order_by('name')]
    unclassified_leaflets = Leaflet.objects.filter(leafletconstituency__constituency__boundary = boundary,
                                                   publisher_party = None)
    if unclassified_leaflets:
        party_list = party_list + [({"name": "Uncategorised"}, unclassified_leaflets)]
    return "boundaries/leaflets.html", {"constituency": boundary.constituency,
                             "party_list": party_list
                             }

def leaflet_colour(n):
    r = math.log((n+1), 2)
    return  (50 + r * 16, 255 - r * 32, 100 + r * 16, 32 + r * 32)

def leaflet_keyvalues():
    return [0,2,5,10,20,50,100,200]


maps = {"leaflets": {"polygon_options": leaflet_polygon_options,
                     "template": leaflet_popup,
                     "colour": leaflet_colour,
                     "keyvalues": leaflet_keyvalues()}
        }

def getDBzoom(z):
    if int(z) > 10:
        return 10
    else:
        return int(z)

def view_key(request, mapname, n, x, y):
    image = Image.new("RGBA", (int(x), int(y)), maps[mapname]["colour"](int(n)))
    response = HttpResponse(mimetype="image/png")
    image.save(response, "PNG")
    return response

def view_map(request, mapname):
    from django.conf import settings
    return render_to_response("boundaries/map.html", {"MEDIA_URL":settings.MEDIA_URL, "mapname": mapname, "keyvalues":maps[mapname]["keyvalues"]})

def tile(request, mapname, tz=None, tx=None, ty=None, tilex=256, tiley = 256):
    options = maps[str(mapname)]
    west, south, east, north = getTileRect(tx, ty, tz)
    zoom = 2 ** float(tz)
    tx = float(tx)
    ty = float(ty)
    image = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    dbz = getDBzoom(tz)

    boundaries_within = Boundary.objects.filter(zoom=dbz, south__lt=north, north__gt=south, east__gt=west, west__lt=east)
    for boundary in boundaries_within:
        polygon_options = options["polygon_options"](boundary)
        coords = eval(boundary.boundary)
        l = []
        for lng, lat in coords:
            x = 256 * (lng - west) / (east - west)
            y = 256 * (lat - north) / (south - north)
            l.append((x, y))
        draw.polygon(l, **polygon_options)
    del draw
    response = HttpResponse(mimetype="image/png")
    image.save(response, "PNG")
    return response

def popup(request, mapname, x=None, y=None, z=None):
    options = maps[str(mapname)]
    x = float(x)
    y = float(y)
    dbz = getDBzoom(z)
    possible_boundaries = Boundary.objects.filter(zoom=int(dbz), south__lt=y, north__gt=y, east__gt=x, west__lt=x)
    for boundary in possible_boundaries:
        coords = eval(boundary.boundary)
        inside = False
        for (vx0, vy0), (vx1, vy1) in zip(coords, coords[1:] + coords[:1]):
            if ((vy0>y) != (vy1>y)) and (x < (vx1-vx0) * (y-vy0) / (vy1-vy0) + vx0):
                inside = not(inside)
        if inside:
            return render_to_response(*options["template"](boundary))
    raise Http404

def to_google(x, tilesAtThisZoom):
  return google_dist * (1 - 2 * float(x) / tilesAtThisZoom)

def getTileRect(xt, yt, zoomt):
           zoom = int(zoomt)
           x = int(xt)
           y = int(yt)
           tilesAtThisZoom = 2 ** zoom

           return (-to_google(x, tilesAtThisZoom),
                   to_google(y + 1, tilesAtThisZoom),
                   -to_google(x + 1, tilesAtThisZoom),
                   to_google(y, tilesAtThisZoom))
