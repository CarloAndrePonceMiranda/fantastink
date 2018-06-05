# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-22 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo_perfil', models.IntegerField()),
                ('descripcion', models.CharField(max_length=255)),
                ('metraje', models.DecimalField(decimal_places=2, max_digits=6)),
                ('desperdicio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('material', models.CharField(max_length=255)),
            ],
        ),
    ]