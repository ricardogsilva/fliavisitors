# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'CAOPContinente.visitors'
        db.add_column('collectvisitors_caopcontinente', 'visitors', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'CAOPContinente.visitors'
        db.delete_column('collectvisitors_caopcontinente', 'visitors')


    models = {
        'collectvisitors.caopcontinente': {
            'Meta': {'object_name': 'CAOPContinente'},
            'dicofre': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'distrito': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'freguesia': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'visitors': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['collectvisitors']
