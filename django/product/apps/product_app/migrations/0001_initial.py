# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-25 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('description', models.TextField(max_length=250)),
                ('weight', models.FloatField(max_length=8)),
                ('price', models.FloatField(max_length=10)),
                ('cost', models.FloatField(max_length=10)),
                ('category', models.TextField(max_length=150)),
            ],
        ),
    ]
