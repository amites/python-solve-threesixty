# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SolveThreeSixty'
        db.create_table('solve_threesixty_solvethreesixty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('solve_id', self.gf('django.db.models.fields.CharField')(max_length=250, null=True)),
        ))
        db.send_create_signal('solve_threesixty', ['SolveThreeSixty'])


    def backwards(self, orm):
        # Deleting model 'SolveThreeSixty'
        db.delete_table('solve_threesixty_solvethreesixty')


    models = {
        'solve_threesixty.solvethreesixty': {
            'Meta': {'object_name': 'SolveThreeSixty'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'solve_id': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'})
        }
    }

    complete_apps = ['solve_threesixty']