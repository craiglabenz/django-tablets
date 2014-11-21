# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tablets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='template',
            options={'ordering': ('name',), 'verbose_name': 'Template', 'verbose_name_plural': 'Templates'},
        ),
        migrations.AddField(
            model_name='template',
            name='level',
            field=models.PositiveIntegerField(default=1, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='template',
            name='lft',
            field=models.PositiveIntegerField(default=1, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='template',
            name='rght',
            field=models.PositiveIntegerField(default=1, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='template',
            name='tree_id',
            field=models.PositiveIntegerField(default=1, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='template',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', blank=True, to='tablets.Template', help_text='Select another template this template should extend.', null=True),
            preserve_default=True,
        ),
    ]
