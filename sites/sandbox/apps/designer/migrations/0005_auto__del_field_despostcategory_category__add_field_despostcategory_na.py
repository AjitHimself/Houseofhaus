# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'DesPostCategory', fields ['designer', 'category']
        db.delete_unique(u'designer_despostcategory', ['designer_id', 'category'])

        # Deleting field 'DesPostCategory.category'
        db.delete_column(u'designer_despostcategory', 'category')

        # Adding field 'DesPostCategory.name'
        db.add_column(u'designer_despostcategory', 'name',
                      self.gf('django.db.models.fields.CharField')(default='default', max_length=30),
                      keep_default=False)

        # Adding field 'DesPostCategory.date_created'
        db.add_column(u'designer_despostcategory', 'date_created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Adding unique constraint on 'DesPostCategory', fields ['designer', 'name']
        db.create_unique(u'designer_despostcategory', ['designer_id', 'name'])


    def backwards(self, orm):
        # Removing unique constraint on 'DesPostCategory', fields ['designer', 'name']
        db.delete_unique(u'designer_despostcategory', ['designer_id', 'name'])

        # Adding field 'DesPostCategory.category'
        db.add_column(u'designer_despostcategory', 'category',
                      self.gf('django.db.models.fields.CharField')(default='def', max_length=30),
                      keep_default=False)

        # Deleting field 'DesPostCategory.name'
        db.delete_column(u'designer_despostcategory', 'name')

        # Deleting field 'DesPostCategory.date_created'
        db.delete_column(u'designer_despostcategory', 'date_created')

        # Adding unique constraint on 'DesPostCategory', fields ['designer', 'category']
        db.create_unique(u'designer_despostcategory', ['designer_id', 'category'])


    models = {
        u'accounts.users': {
            'Meta': {'object_name': 'Users'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_designer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'designer.designer': {
            'Meta': {'object_name': 'Designer'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'designer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.Users']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'profile_pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'designer.designerpost': {
            'Meta': {'object_name': 'DesignerPost'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'categ'", 'null': 'True', 'to': u"orm['designer.DesPostCategory']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'designer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'des'", 'to': u"orm['designer.Designer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'post_status': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        u'designer.despostcategory': {
            'Meta': {'unique_together': "(('designer', 'name'),)", 'object_name': 'DesPostCategory'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'designer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'desig'", 'to': u"orm['designer.Designer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '30'})
        },
        u'designer.despostimage': {
            'Meta': {'object_name': 'DesPostImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'postimage'", 'to': u"orm['designer.DesignerPost']"})
        },
        u'designer.desvideourl': {
            'Meta': {'object_name': 'DesVideoUrl'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'postvideo'", 'to': u"orm['designer.DesignerPost']"}),
            'video_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['designer']