# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Website'
        db.create_table(u'extwebsite_website', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('domain', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('app_id', self.gf('django.db.models.fields.BigIntegerField')()),
            ('app_secret', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ga_id', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('is_valid', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'extwebsite', ['Website'])


    def backwards(self, orm):
        # Deleting model 'Website'
        db.delete_table(u'extwebsite_website')


    models = {
        u'extwebsite.website': {
            'Meta': {'object_name': 'Website'},
            'app_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'app_secret': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ga_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_valid': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['extwebsite']