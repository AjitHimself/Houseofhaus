# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'DesignerRequest.profile_pic'
        db.delete_column(u'request_designerrequest', 'profile_pic')

        # Deleting field 'DesignerRequest.gender'
        db.delete_column(u'request_designerrequest', 'gender')


    def backwards(self, orm):
        # Adding field 'DesignerRequest.profile_pic'
        db.add_column(u'request_designerrequest', 'profile_pic',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DesignerRequest.gender'
        db.add_column(u'request_designerrequest', 'gender',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True),
                      keep_default=False)


    models = {
        u'request.designerrequest': {
            'Meta': {'object_name': 'DesignerRequest'},
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'date_requested': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'speciality': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['request']