# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ExtendedUser'
        db.create_table(u'extfacebook_extendeduser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=90, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=90, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=200)),
            ('facebook_id', self.gf('django.db.models.fields.BigIntegerField')()),
            ('access_token', self.gf('django.db.models.fields.TextField')()),
            ('app_id', self.gf('django.db.models.fields.BigIntegerField')(default=0, db_index=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('raw_facebook_profile', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'extfacebook', ['ExtendedUser'])

        # Adding model 'FacebookFanpage'
        db.create_table(u'extfacebook_facebookfanpage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('fanpage_url', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('is_valid', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'extfacebook', ['FacebookFanpage'])


    def backwards(self, orm):
        # Deleting model 'ExtendedUser'
        db.delete_table(u'extfacebook_extendeduser')

        # Deleting model 'FacebookFanpage'
        db.delete_table(u'extfacebook_facebookfanpage')


    models = {
        u'extfacebook.extendeduser': {
            'Meta': {'object_name': 'ExtendedUser'},
            'access_token': ('django.db.models.fields.TextField', [], {}),
            'app_id': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '200'}),
            'facebook_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '90', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '90', 'blank': 'True'}),
            'raw_facebook_profile': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'extfacebook.facebookfanpage': {
            'Meta': {'object_name': 'FacebookFanpage'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fanpage_url': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_valid': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['extfacebook']