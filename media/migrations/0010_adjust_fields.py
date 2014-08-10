# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

DEFAULT_OPTIONS = {'max_length': 255, 'blank': True, 'default': ''}

ADD_COLUMNS = {
    'barcode': {'fieldType': 'django.db.models.fields.IntegerField', 'options': {}},
    'contenttype': {'fieldType': 'django.db.models.fields.CharField', 'options': DEFAULT_OPTIONS},
    'language': {'fieldType': 'django.db.models.fields.CharField', 'options': DEFAULT_OPTIONS},
    'md5': {'fieldType': 'django.db.models.fields.CharField', 'options': DEFAULT_OPTIONS},
    'releasedate': {'fieldType': 'django.db.models.fields.DateField', 'options': {}},
    'version': {'fieldType': 'django.db.models.fields.CharField', 'options': DEFAULT_OPTIONS},
}

DELETE_COLUMNS = {
    'content': {'fieldType': 'django.db.models.fields.TextField', 'options': {'blank': True}},
    'created_at': {'fieldType': 'django.db.models.fields.DateTimeField', 'options': {}},
    'published': {'fieldType': 'django.db.models.fields.BooleanField', 'options': {}},
    'updated_at': {'fieldType': 'django.db.models.fields.DateTimeField', 'options': {}},
}


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding fields.
        for col, values in ADD_COLUMNS.iteritems():
            db.add_column(
                'media_media',
                col,
                self.gf(values['fieldType'])(**values['options']),
            )

        # Deleting fields.
        for col in DELETE_COLUMNS.keys():
            db.delete_column('media_media', col)

    def backwards(self, orm):
        # Adding fields.
        for col, values in DELETE_COLUMNS.iteritems():
            db.add_column(
                'media_media',
                col,
                self.gf(values['fieldType'])(**values['options']),
            )

        # Deleting fields.
        for col in ADD_COLUMNS.keys():
            db.delete_column('media_media', col)

    models = {
        u'media.media': {
            'Meta': {'object_name': 'Media'},
            'barcode': ('django.db.models.fields.IntegerField', [], {}),
            'contenttype': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'md5': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'releasedate': ('django.db.models.fields.DateField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['media']