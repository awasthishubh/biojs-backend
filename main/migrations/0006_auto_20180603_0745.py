# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-03 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20180603_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='license',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='component',
            name='version',
            field=models.CharField(max_length=50, null=True),
        ),
    ]