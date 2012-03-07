from django.contrib.gis import admin
from models import *

class CAOPContinenteAdmin(admin.GeoModelAdmin):
    list_display = ('freguesia', 'municipio', 'distrito', 'visitors')

admin.site.register(CAOPContinente, CAOPContinenteAdmin)
