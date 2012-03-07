# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'CAOPContinente'
        db.create_table('collectvisitors_caopcontinente', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dicofre', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('freguesia', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('municipio', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('distrito', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal('collectvisitors', ['CAOPContinente'])


    def backwards(self, orm):
        
        # Deleting model 'CAOPContinente'
        db.delete_table('collectvisitors_caopcontinente')


    models = {
        'collectvisitors.caopcontinente': {
            'Meta': {'object_name': 'CAOPContinente'},
            'dicofre': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'distrito': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'freguesia': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['collectvisitors']
