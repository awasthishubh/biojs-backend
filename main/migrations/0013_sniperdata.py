# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-25 07:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20180624_0930'),
    ]

    operations = [
        migrations.CreateModel(
            name='SniperData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_browserify', models.BooleanField(default=False)),
                ('wzrd_url', models.URLField(null=True)),
                ('component', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Component')),
            ],
        ),
    ]
