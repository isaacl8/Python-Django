# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-29 22:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secret_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='secret',
            old_name='context',
            new_name='content',
        ),
    ]
