from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core import serializers
from django.core.urlresolvers import reverse
from django.contrib.gis.geos import Point
from models import CAOPContinente
from forms import VoteForm

def index(request):
    return render_to_response('collectvisitors/map.html',
                              context_instance=RequestContext(request))

def xhr_vote_popup(request, lon, lat):
    p = Point(float(lon), float(lat))
    freguesia = CAOPContinente.objects.get(geometry__intersects=p)
    print("xhr_vote_popup: request.method: %s" % request.method)
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            num_visitors = form.cleaned_data['adicionar_visitantes']
            freguesia.visitors += int(num_visitors)
            freguesia.save()
            result = HttpResponseRedirect(
                        #reverse('collectvisitors.views.xhr_vote_ok'), 
                        reverse('collectvisitors-vote_ok', args=(freguesia.pk,))
                     )
        else:
            form = VoteForm()
            result = render_to_response(
                        'collectvisitors/voteform.html',
                        {'form' : form, 'freguesia' : freguesia}, 
                        context_instance=RequestContext(request)
                     )
    else:
        form = VoteForm()
        result = render_to_response(
                    'collectvisitors/voteform.html',
                    {'form' : form, 'freguesia' : freguesia}, 
                    context_instance=RequestContext(request)
                 )
    return result

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

def xhr_vote(request, freg_id):
    freg_id = int(freg_id)
    freguesia = CAOPContinente.objects.get(pk=freg_id)
    print("xhr_vote: request.method: %s" % request.method)
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            #freg_id = form.cleaned_data['freguesia']
            num_visitors = form.cleaned_data['adicionar_visitantes']
            freguesia.visitors += int(num_visitors)
            freguesia.save()
            result = HttpResponseRedirect(
                        #reverse('collectvisitors.views.xhr_vote_ok'), 
                        reverse('collectvisitors-vote_ok', args=(freg_id,))
                        #reverse('collectvisitors-vote', args=(freg_id,))
                     )
        else:
            form = VoteForm()
            result = render_to_response(
                        'collectvisitors/voteform.html',
                        {'form' : form}, 
                        context_instance=RequestContext(request)
                     )
    else:
        form = VoteForm()
        result = render_to_response(
                    'collectvisitors/voteform.html',
                    {'form' : form, 'freguesia' : freguesia}, 
                    context_instance=RequestContext(request)
                 )
    return result

def xhr_vote_ok(request, freg_id):
    freguesia = CAOPContinente.objects.filter(pk=freg_id)
    result = render_to_response(
                'collectvisitors/voteok.html',
                {'freguesia' : freguesia}, 
                context_instance=RequestContext(request)
             )
    return result
