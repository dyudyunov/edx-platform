# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-04-01 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tedix_ro', '0006_auto_20190329_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
