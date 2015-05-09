# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteOptions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=100, help_text='The title of your comic', default='Cube Drone')),
                ('tagline', models.CharField(max_length=100, help_text='A short tagline for your comic', default='Code/comics, updates Tuesday & Thursday')),
                ('elevator_pitch', models.TextField(help_text='A Tweet-length description of your comic.', default='Comics about software development in a small Vancouver startup.')),
                ('email', models.CharField(max_length=100, help_text='The site sends e-mail drom this address.', default='curtis@lassam.net')),
                ('author_name', models.CharField(max_length=100, help_text="What's the author (or author's) names?", default='Curtis Lassam')),
                ('author_website', models.CharField(max_length=100, help_text='Does the author have a personal website?', default='http://curtis.lassam.net')),
                ('mobile_logo_url', models.CharField(max_length=200, help_text='The URL for the mobile-sized (width:300px, height:100px) logo to the website.', default='http://butts.butts/butts.jpg')),
                ('desktop_logo_url', models.CharField(max_length=200, help_text='The URL for the desktop-sized (width:500px, height:100px) logo to the website.', default='http://butts.butts/deskbutts.jpg')),
                ('google_tracking_code', models.CharField(max_length=50, default='UA-41279849-1')),
                ('twitter_username', models.CharField(max_length=50, default='classam')),
                ('twitter_widget_id', models.CharField(max_length=50, default='304715092187025408')),
            ],
        ),
    ]
