# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-19 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_onerror', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='onerrorreportinfo',
            name='extra',
            field=models.TextField(blank=True, help_text='\u989d\u5916\u4fe1\u606f', null=True, verbose_name='extra'),
        ),
    ]
