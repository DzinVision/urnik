# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urnik', '0008_auto_20170927_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='ucilnica',
            name='kratka_oznaka',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]