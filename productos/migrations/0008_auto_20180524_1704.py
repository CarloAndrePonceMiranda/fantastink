# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-24 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0007_auto_20180524_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='descripcion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='nombre',
            field=models.CharField(max_length=50, null=True),
        ),
    ]