# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-10-24 07:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VGI', '0006_criteria_create_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='criteria',
            options={'ordering': ('-create_date',)},
        ),
    ]
