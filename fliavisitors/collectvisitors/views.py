from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core import serializers
from django.contrib.gis.geos import Point
from models import CAOPContinente

def index(request):
    return render_to_response('collectvisitors/map.html',
                              context_instance=RequestContext(request))

def xhr_freguesia(request, lon, lat):
    '''
    Return selected freguesia in JSON format.
    '''

    #if request.is_ajax():
    mimetype = 'application/javascript'
    p = Point(float(lon), float(lat))
    freguesias = CAOPContinente.objects.filter(geometry__intersects=p)
    data = serializers.serialize('json', freguesias, ensure_ascii=False,
                                 fields=('freguesia', 'visitors'))
    result = HttpResponse(data, mimetype)
    #else:
    #    result = HttpResponse(status=400)
    return result

def xhr_top_visitors(request):
    '''Return the five freguesias with most visitors.'''

    #if request.is_ajax():
    mimetype = 'application/javascript'
    freguesias = CAOPContinente.objects.order_by('-visitors')[:5]
    data = serializers.serialize('json', freguesias, ensure_ascii=False, 
                                 fields=('freguesia', 'visitors'))
    result = HttpResponse(data, mimetype)
    #else:
    #    result = HttpResponse(status=400)
    return result

