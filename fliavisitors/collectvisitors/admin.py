from django.contrib.gis import admin
from models import *

admin.site.register(CAOPContinente, admin.GeoModelAdmin)
