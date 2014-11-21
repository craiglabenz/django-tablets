# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Template'
        db.create_table(u'tablets_template', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('template_engine', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'children', null=True, to=orm['tablets.Template'])),
            ('default_context', self.gf('annoying.fields.JSONField')(default=u'{}', blank=True)),
        ))
        db.send_create_signal(u'tablets', ['Template'])

    def backwards(self, orm):
        # Deleting model 'Template'
        db.delete_table(u'tablets_template')

    models = {
        u'tablets.template': {
            'Meta': {'object_name': 'Template'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'default_context': ('annoying.fields.JSONField', [], {'default': "u'{}'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['tablets.Template']"}),
            'template_engine': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['tablets']