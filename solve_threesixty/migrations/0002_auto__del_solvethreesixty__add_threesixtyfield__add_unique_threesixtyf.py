# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'SolveThreeSixty'
        db.delete_table('solve_threesixty_solvethreesixty')

        # Adding model 'ThreeSixtyField'
        db.create_table('solve_threesixty_threesixtyfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('solve_id', self.gf('django.db.models.fields.CharField')(max_length=250, null=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
        ))
        db.send_create_signal('solve_threesixty', ['ThreeSixtyField'])

        # Adding unique constraint on 'ThreeSixtyField', fields ['solve_id', 'type']
        db.create_unique('solve_threesixty_threesixtyfield', ['solve_id', 'type'])

        # Adding model 'ThreeSixtyContact'
        db.create_table('solve_threesixty_threesixtycontact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('solve_id', self.gf('django.db.models.fields.CharField')(max_length=250, null=True)),
        ))
        db.send_create_signal('solve_threesixty', ['ThreeSixtyContact'])

        # Adding model 'ThreeSixtyTag'
        db.create_table('solve_threesixty_threesixtytag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('solve_id', self.gf('django.db.models.fields.CharField')(max_length=250, null=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
        ))
        db.send_create_signal('solve_threesixty', ['ThreeSixtyTag'])

        # Adding unique constraint on 'ThreeSixtyTag', fields ['solve_id', 'type']
        db.create_unique('solve_threesixty_threesixtytag', ['solve_id', 'type'])

        # Adding model 'ThreeSixtyUser'
        db.create_table('solve_threesixty_threesixtyuser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('solve_id', self.gf('django.db.models.fields.CharField')(max_length=250, null=True)),
        ))
        db.send_create_signal('solve_threesixty', ['ThreeSixtyUser'])


    def backwards(self, orm):
        # Removing unique constraint on 'ThreeSixtyTag', fields ['solve_id', 'type']
        db.delete_unique('solve_threesixty_threesixtytag', ['solve_id', 'type'])

        # Removing unique constraint on 'ThreeSixtyField', fields ['solve_id', 'type']
        db.delete_unique('solve_threesixty_threesixtyfield', ['solve_id', 'type'])

        # Adding model 'SolveThreeSixty'
        db.create_table('solve_threesixty_solvethreesixty', (
            ('solve_id', self.gf('django.db.models.fields.CharField')(max_length=250, null=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('solve_threesixty', ['SolveThreeSixty'])

        # Deleting model 'ThreeSixtyField'
        db.delete_table('solve_threesixty_threesixtyfield')

        # Deleting model 'ThreeSixtyContact'
        db.delete_table('solve_threesixty_threesixtycontact')

        # Deleting model 'ThreeSixtyTag'
        db.delete_table('solve_threesixty_threesixtytag')

        # Deleting model 'ThreeSixtyUser'
        db.delete_table('solve_threesixty_threesixtyuser')


    models = {
        'solve_threesixty.threesixtycontact': {
            'Meta': {'object_name': 'ThreeSixtyContact'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'solve_id': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'})
        },
        'solve_threesixty.threesixtyfield': {
            'Meta': {'ordering': "('type',)", 'unique_together': "(('solve_id', 'type'),)", 'object_name': 'ThreeSixtyField'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'solve_id': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        'solve_threesixty.threesixtytag': {
            'Meta': {'ordering': "('type',)", 'unique_together': "(('solve_id', 'type'),)", 'object_name': 'ThreeSixtyTag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'solve_id': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        'solve_threesixty.threesixtyuser': {
            'Meta': {'object_name': 'ThreeSixtyUser'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'solve_id': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'})
        }
    }

    complete_apps = ['solve_threesixty']