# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-17 21:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indiatoday',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='indiatoday',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='indiatoday',
            old_name='Headline',
            new_name='headline',
        ),
        migrations.RenameField(
            model_name='indiatoday',
            old_name='Link',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='indiatoday',
            old_name='Sentiment',
            new_name='sentiment',
        ),
        migrations.RenameField(
            model_name='ndtv',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='ndtv',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='ndtv',
            old_name='Headline',
            new_name='headline',
        ),
        migrations.RenameField(
            model_name='ndtv',
            old_name='Link',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='ndtv',
            old_name='Sentiment',
            new_name='sentiment',
        ),
        migrations.RenameField(
            model_name='republic',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='republic',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='republic',
            old_name='Link',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='republic',
            old_name='Sentiment',
            new_name='sentiment',
        ),
    ]
