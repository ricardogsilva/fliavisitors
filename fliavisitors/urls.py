from django.conf.urls.defaults import patterns, include, url
from django.contrib.gis import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fliavisitors.views.home', name='home'),
    # url(r'^fliavisitors/', include('fliavisitors.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^visitantes/', include('collectvisitors.urls')),
)

#urlpatterns += patterns('',
#    (r'^(?P<url>.*)$', 'httpproxy.views.proxy'),
#)
