# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-25 16:34
from __future__ import unicode_literals

from django.db import migrations, models
import productos.models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0016_auto_20180525_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelo',
            name='imagen',
            field=models.FileField(blank=True, null=True, upload_to=productos.models.upload_image_path),
        ),
    ]