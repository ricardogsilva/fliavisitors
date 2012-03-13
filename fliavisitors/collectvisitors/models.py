from django.contrib.gis.db import models

class CAOPContinente(models.Model):
    dicofre = models.CharField(max_length=7)
    freguesia = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)
    distrito = models.CharField(max_length=255)
    geometry = models.MultiPolygonField()
    objects = models.GeoManager()
    visitors = models.IntegerField(default=0, db_index=True)

    def __unicode__(self):
        return self.freguesia
