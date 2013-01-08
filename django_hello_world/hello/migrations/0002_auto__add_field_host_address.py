# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Host.address'
        db.add_column('hello_host', 'address',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2013, 1, 8, 0, 0), max_length=128),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Host.address'
        db.delete_column('hello_host', 'address')


    models = {
        'hello.host': {
            'Meta': {'object_name': 'Host'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['hello']