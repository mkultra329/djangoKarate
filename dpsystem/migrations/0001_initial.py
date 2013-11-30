# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Student'
        db.create_table('dpsystem_student', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('dpsystem', ['Student'])

        # Adding model 'Dojo'
        db.create_table('dpsystem_dojo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dojo_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('dpsystem', ['Dojo'])


    def backwards(self, orm):
        # Deleting model 'Student'
        db.delete_table('dpsystem_student')

        # Deleting model 'Dojo'
        db.delete_table('dpsystem_dojo')


    models = {
        'dpsystem.dojo': {
            'Meta': {'object_name': 'Dojo'},
            'dojo_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'dpsystem.student': {
            'Meta': {'object_name': 'Student'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['dpsystem']