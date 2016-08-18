# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webfai', '0004_auto_20160713_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='addr',
            field=models.CharField(max_length=17, verbose_name='Adresse MAC'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Nom'),
        ),
    ]
