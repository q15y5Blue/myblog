# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='travels',
            name='travel_url',
            field=models.CharField(default='travel_url', max_length=1000),
        ),
    ]
