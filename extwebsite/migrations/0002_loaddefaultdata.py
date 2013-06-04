# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        orm['extwebsite.website'](
            app_id = 118455931682587,
            app_secret = '461e2dfc5a01cf2108beacc02226e86c',
            domain = 'localhost:8000',
            ga_id = 'None',
            is_valid = True
        ).save()


    def backwards(self, orm):
        orm['extwebsite.website'].objects.get(app_id=118455931682587).delete()

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
    symmetrical = True
