from django.conf.urls.defaults import *

urlpatterns = patterns('collectvisitors.views',
    url(r'^$', 'index'),
    url(r'^xhr/(?P<lon>-?\d+\.?\d*)/(?P<lat>\d+\.?\d*)/$', 'xhr_freguesia'),
    url(r'^xhr/topvisitors/$', 'xhr_top_visitors'),
 )
