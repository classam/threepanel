# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('posted', models.DateTimeField(db_index=True)),
                ('image_url', models.CharField(max_length=300)),
                ('secret_text', models.TextField(default='', blank=True)),
                ('alt_text', models.TextField(default='', blank=True)),
                ('hidden', models.BooleanField(default=False)),
                ('slug', autoslug.fields.AutoSlugField(editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]