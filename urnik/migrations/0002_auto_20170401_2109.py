# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-01 21:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urnik', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='srecanje',
            name='dan',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'ponedeljek'), (2, 'torek'), (3, 'sreda'), (4, 'četrtek'), (5, 'petek')]),
        ),
    ]