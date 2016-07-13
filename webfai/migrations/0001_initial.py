# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 07:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Installation', 'INSTALL'), ('Mise \xe0 jour', 'MAJ')], max_length=20, verbose_name='FAI Action')),
            ],
        ),
        migrations.CreateModel(
            name='Archi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('x32', 'I386'), ('x64', 'AMD64')], max_length=20, verbose_name='Architecture')),
            ],
        ),
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Local', 'LOCAL'), ('Ldap', 'LDAP')], max_length=10, verbose_name='Authentification')),
            ],
        ),
        migrations.CreateModel(
            name='Clavier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Fr', 'AZERTY'), ('Us', 'QWERTY'), ('Uk', 'QWERTY_UK')], max_length=20, verbose_name='Clavier')),
            ],
        ),
        migrations.CreateModel(
            name='Distrib',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Stable', 'JESSIE'), ('Testing', 'STRETCH')], max_length=20, verbose_name='Distribution')),
            ],
        ),
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Airsea', 'EQUIPE_AIRSEA'), ('Casys', 'EQUIPE_CASYS'), ('Cvgi', 'EQUIPE_CVGI'), ('Dea', 'EQUIPE_DEA'), ('Edp', 'EQUIPE_EDP'), ('Ips', 'EQUIPE_IPS'), ('Sagag', 'EQUIPE_SAGAG'), ('Sam', 'EQUIPE_SAM'), ('Staff', 'EQUIPE_STAFF')], max_length=30, verbose_name='Equipe')),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nom')),
                ('addr', models.CharField(max_length=17, verbose_name='Adresse MAC')),
                ('gl_drivers', models.BooleanField(default=False, verbose_name='Drivers Nvidia OpenGL')),
                ('action', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webfai.Action', verbose_name='FAI Action')),
                ('archi', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webfai.Archi', verbose_name='Architecture')),
                ('auth', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webfai.Auth', verbose_name='Authentification')),
                ('clavier', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webfai.Clavier', verbose_name='Clavier')),
                ('distri', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webfai.Distrib', verbose_name='Distribution')),
                ('equipe', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webfai.Equipe', verbose_name='Equipe')),
            ],
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Station', 'LJK_STATION'), ('Serveur de Calcul', 'LJK_SERV_CALCUL'), ('Serveur', 'LJK_SERV')], max_length=30, verbose_name='Profil')),
            ],
        ),
        migrations.CreateModel(
            name='Wm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Tous', 'TOUS'), ('Gnome', 'GNOME'), ('Kde', 'KDE'), ('IceWM', 'ICEWM'), ('Enlightenment', 'E17')], max_length=20, verbose_name='Window Manager')),
            ],
        ),
        migrations.AddField(
            model_name='machine',
            name='profil',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webfai.Profil', verbose_name='Profil'),
        ),
        migrations.AddField(
            model_name='machine',
            name='wm',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webfai.Wm', verbose_name='Window Manager'),
        ),
    ]
