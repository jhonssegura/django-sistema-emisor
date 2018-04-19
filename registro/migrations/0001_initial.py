# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-04-19 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_ana', models.CharField(max_length=7, verbose_name='Código del Analista')),
                ('ana_ced', models.IntegerField(verbose_name='Cédula de Identidad')),
                ('ana_nom', models.CharField(max_length=200, verbose_name='Nombres')),
                ('ana_ape', models.CharField(max_length=200, verbose_name='Apellidos')),
                ('ana_activo', models.BooleanField(verbose_name='¿Se encuentra activo?')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_cur', models.CharField(max_length=200, unique=True, verbose_name='Código Indentificación')),
                ('cur_nom', models.CharField(max_length=200, verbose_name='Nombre del Curso')),
                ('cur_date_ini', models.DateField(blank=True, null=True, verbose_name='Fecha de Inicio')),
                ('cur_date_fin', models.DateField(blank=True, null=True, verbose_name='Fecha Finalización')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_even', models.CharField(max_length=200, unique=True, verbose_name='Código Indentificación')),
                ('even_nom', models.CharField(max_length=200, verbose_name='Nombre del Evento')),
                ('even_date_ini', models.DateField(blank=True, null=True, verbose_name='Fecha de Inicio')),
                ('even_date_fin', models.DateField(blank=True, null=True, verbose_name='Fecha de Finalización')),
                ('even_site', models.TextField(blank=True, max_length=500, null=True, verbose_name='Lugar del EVento')),
                ('even_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_lib', models.CharField(max_length=200, unique=True, verbose_name='Código Indentificación')),
                ('lib_nom', models.CharField(max_length=200, verbose_name='Título del Libro')),
                ('lib_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Publicación')),
                ('lib_cenditel', models.BooleanField(verbose_name='¿Realizado en CENDITEL?')),
                ('lib_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='URL Visualización')),
            ],
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_part', models.CharField(max_length=10, unique=True, verbose_name='Código del Participante')),
                ('part_ced', models.CharField(max_length=200, unique=True, verbose_name='Cédula de Identidad')),
                ('part_nom', models.CharField(max_length=200, verbose_name='Nombres')),
                ('part_ape', models.CharField(max_length=200, verbose_name='Apellidos')),
                ('part_cor', models.EmailField(max_length=254, verbose_name='Correo Electrónico')),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_pto', models.CharField(max_length=200, unique=True, verbose_name='Código Indentificación')),
                ('pto_nom', models.CharField(max_length=200, verbose_name='Nombre del Proyecto')),
                ('pto_date_ini', models.DateField(blank=True, null=True, verbose_name='Fecha de Inicio')),
                ('pto_date_fin', models.DateField(blank=True, null=True, verbose_name='Fecha Finalización')),
                ('pto_poa', models.BooleanField(verbose_name='¿Pertenece al POA?')),
            ],
        ),
        migrations.CreateModel(
            name='Revista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rev_num', models.CharField(max_length=200, unique=True, verbose_name='Número de la Revista')),
                ('rev_nom', models.CharField(max_length=200, verbose_name='Título de la Revista')),
                ('rev_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Publicación')),
                ('rev_arb', models.BooleanField(verbose_name='¿Revista Arbitrada?')),
                ('rev_cenditel', models.BooleanField(verbose_name='¿Realizado en CENDITEL?')),
                ('rev_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='URL Visualización')),
            ],
        ),
        migrations.AddField(
            model_name='evento',
            name='even_part',
            field=models.ManyToManyField(to='registro.Participante'),
        ),
        migrations.AddField(
            model_name='curso',
            name='cur_ins',
            field=models.ManyToManyField(to='registro.Participante'),
        ),
        migrations.AddField(
            model_name='analista',
            name='ana_pro',
            field=models.ManyToManyField(to='registro.Proyecto'),
        ),
    ]
