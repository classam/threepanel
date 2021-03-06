# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-20 04:48
from __future__ import unicode_literals

import autoslug.fields
import dashboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20160219_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteoptions',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='cube-drone', editable=False, populate_from=models.CharField(default='Cube Drone', help_text='The title of your comic', max_length=100), slugify=dashboard.models.slugify, unique=True),
        ),
    ]
