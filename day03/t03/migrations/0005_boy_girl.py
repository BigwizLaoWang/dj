# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-15 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t03', '0004_author_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('age', models.IntegerField(verbose_name='\u5e74\u7eaa')),
                ('height', models.FloatField(verbose_name='height')),
                ('salary', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Girl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('age', models.IntegerField(verbose_name='\u5e74\u7eaa')),
                ('height', models.FloatField(verbose_name='height')),
                ('face_score', models.IntegerField(verbose_name='yanzhi')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]