from django.conf.urls.defaults import *

urlpatterns = patterns('collectvisitors.views',
    url(r'^$', 'index'),
    #url(r'^xhr/(?P<lon>-?\d+\.?\d*)/(?P<lat>\d+\.?\d*)/$', 'xhr_freguesia'),
    url(r'^xhr/(?P<lon>-?\d+\.?\d*)/(?P<lat>\d+\.?\d*)/$', 'xhr_vote_popup', name='collectvisitors-vote_popup'),
    url(r'^xhr/topvisitors/$', 'xhr_top_visitors'),
    url(r'^xhr/(?P<freg_id>\d+)/vote/$', 'xhr_vote', name='collectvisitors-vote'),
    url(r'^xhr/(?P<freg_id>\d+)/ok/$', 'xhr_vote_ok', name='collectvisitors-vote_ok'),
 )
