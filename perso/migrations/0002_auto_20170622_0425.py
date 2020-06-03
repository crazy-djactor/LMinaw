# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 02:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perso', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='descr',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=64, verbose_name='nom'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='added',
            field=models.DateTimeField(auto_now_add=True, verbose_name='ajouté'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='content',
            field=models.TextField(blank=True, verbose_name='contenu'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='modif',
            field=models.DateTimeField(auto_now=True, verbose_name='modifié'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='slug',
            field=models.SlugField(verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='title',
            field=models.CharField(max_length=64, verbose_name='titre'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=16, verbose_name='nom'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(verbose_name='slug'),
        ),
    ]
