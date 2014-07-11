# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'DesignerRequest.date_joined'
        db.delete_column(u'request_designerrequest', 'date_joined')

        # Adding field 'DesignerRequest.email'
        db.add_column(u'request_designerrequest', 'email',
                      self.gf('django.db.models.fields.EmailField')(max_length=75, unique=True, null=True),
                      keep_default=False)

        # Adding field 'DesignerRequest.date_requested'
        db.add_column(u'request_designerrequest', 'date_requested',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'DesignerRequest.date_joined'
        db.add_column(u'request_designerrequest', 'date_joined',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'DesignerRequest.email'
        db.delete_column(u'request_designerrequest', 'email')

        # Deleting field 'DesignerRequest.date_requested'
        db.delete_column(u'request_designerrequest', 'date_requested')


    models = {
        u'request.designerrequest': {
            'Meta': {'object_name': 'DesignerRequest'},
            'date_requested': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'unique': 'True', 'null': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'profile_pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'speciality': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'})
        }
    }

    complete_apps = ['request']