# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-11 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_auto_20181216_1855'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexTop10',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.TextField()),
            ],
        ),
    ]
