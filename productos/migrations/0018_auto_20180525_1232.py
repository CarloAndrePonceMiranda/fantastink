# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-25 17:32
from __future__ import unicode_literals

from django.db import migrations, models
import productos.models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0017_auto_20180525_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=productos.models.upload_image_path),
        ),
    ]