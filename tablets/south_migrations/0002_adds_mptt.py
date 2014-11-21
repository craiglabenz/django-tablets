# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Template.lft'
        db.add_column(u'tablets_template', u'lft',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True),
                      keep_default=False)

        # Adding field 'Template.rght'
        db.add_column(u'tablets_template', u'rght',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True),
                      keep_default=False)

        # Adding field 'Template.tree_id'
        db.add_column(u'tablets_template', u'tree_id',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True),
                      keep_default=False)

        # Adding field 'Template.level'
        db.add_column(u'tablets_template', u'level',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True),
                      keep_default=False)


        # Changing field 'Template.parent'
        db.alter_column(u'tablets_template', 'parent_id', self.gf('mptt.fields.TreeForeignKey')(null=True, to=orm['tablets.Template']))

    def backwards(self, orm):
        # Deleting field 'Template.lft'
        db.delete_column(u'tablets_template', u'lft')

        # Deleting field 'Template.rght'
        db.delete_column(u'tablets_template', u'rght')

        # Deleting field 'Template.tree_id'
        db.delete_column(u'tablets_template', u'tree_id')

        # Deleting field 'Template.level'
        db.delete_column(u'tablets_template', u'level')


        # Changing field 'Template.parent'
        db.alter_column(u'tablets_template', 'parent_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['tablets.Template']))

    models = {
        u'tablets.template': {
            'Meta': {'object_name': 'Template'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'default_context': ('annoying.fields.JSONField', [], {'default': "u'{}'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['tablets.Template']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'template_engine': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['tablets']