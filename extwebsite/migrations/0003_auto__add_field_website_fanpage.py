# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Website.fanpage'
        db.add_column(u'extwebsite_website', 'fanpage',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['extfacebook.FacebookFanpage'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Website.fanpage'
        db.delete_column(u'extwebsite_website', 'fanpage_id')


    models = {
        u'extfacebook.facebookfanpage': {
            'Meta': {'object_name': 'FacebookFanpage'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fanpage_url': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_valid': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'extwebsite.website': {
            'Meta': {'object_name': 'Website'},
            'app_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'app_secret': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fanpage': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['extfacebook.FacebookFanpage']", 'null': 'True', 'blank': 'True'}),
            'ga_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_valid': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['extwebsite']