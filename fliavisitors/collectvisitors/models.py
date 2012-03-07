from django.contrib.gis.db import models

class CAOPContinente(models.Model):
    dicofre = models.CharField(max_length=7)
    freguesia = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)
    distrito = models.CharField(max_length=255)
    #taa = models.CharField(max_length=255)
    #area_ea_ha = models.FloatField()
    #area_t_ha = models.FloatField()

    geometry = models.MultiPolygonField()
    objects = models.GeoManager()

    def __unicode__(self):
        return self.freguesia
