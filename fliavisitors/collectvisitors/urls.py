from django.conf.urls.defaults import *

urlpatterns = patterns('collectvisitors.views',
    url(r'^$', 'index'),
 )
