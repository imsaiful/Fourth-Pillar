# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-15 22:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_auto_20181216_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ndtv',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
