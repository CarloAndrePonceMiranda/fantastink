# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-25 15:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0013_modelo'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelo',
            name='perfil',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.Perfil'),
        ),
    ]
