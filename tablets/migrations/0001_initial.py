# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import annoying.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('template_engine', models.IntegerField(default=1, verbose_name='Template Engine', choices=[(1, 'Django'), (2, 'Jinja2')])),
                ('default_context', annoying.fields.JSONField(default='{}', verbose_name='Default Context', blank=True)),
                ('parent', models.ForeignKey(related_name='children', blank=True, to='tablets.Template', help_text='Select another template this template should extend.', null=True)),
            ],
            options={
                'verbose_name': 'Template',
                'verbose_name_plural': 'Templates',
            },
            bases=(models.Model,),
        ),
    ]
