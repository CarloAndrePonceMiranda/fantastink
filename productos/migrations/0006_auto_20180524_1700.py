# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-24 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_auto_20180524_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='descripcion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='metraje',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
