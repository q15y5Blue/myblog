# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 02:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identify', models.IntegerField(default='user_identify_id', unique=True)),
                ('name', models.CharField(default='user_name', max_length=32)),
                ('describe', models.CharField(default='user_describe', max_length=1000)),
                ('followings', models.TextField()),
                ('fans', models.TextField()),
                ('followings_number', models.IntegerField(default='user_followings_numbers')),
                ('fans_number', models.IntegerField(default='user_fans_numbers')),
            ],
        ),
        migrations.CreateModel(
            name='TravelCatContentComments',
            fields=[
                ('comments_id', models.AutoField(max_length=128, primary_key=True, serialize=False)),
                ('comments_datetime', models.DateTimeField(default='comments_time')),
                ('comment_f_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Travels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travel_create_data', models.DateField(default='travel_create_data')),
                ('travel_view_number', models.IntegerField(default='travel_view_number')),
                ('travel_commended', models.BooleanField(default='travel_commend')),
                ('travel_when', models.DateField(default='travel_date')),
                ('travel_how_long', models.IntegerField(default='travel_spend_time')),
                ('travel_how_much', models.IntegerField(default='travel_cost')),
                ('travel_who', models.CharField(default='travel_who', max_length=30)),
                ('travel_how', models.CharField(default='travel_how', max_length=30)),
                ('travel_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Persons')),
            ],
        ),
        migrations.CreateModel(
            name='TravelsCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalog_title', models.CharField(default='travel_catalog_title', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='TravelsCatalogContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.CharField(default='travel_cat_type', max_length=64)),
                ('content_title', models.CharField(default='travel_cat_content', max_length=128)),
                ('content_content', models.TextField(default='travel_content')),
                ('content_catalog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.TravelsCatalog')),
            ],
        ),
        migrations.AddField(
            model_name='travelcatcontentcomments',
            name='comment_content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.TravelsCatalogContent'),
        ),
        migrations.AddField(
            model_name='travelcatcontentcomments',
            name='comments_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Persons'),
        ),
    ]
