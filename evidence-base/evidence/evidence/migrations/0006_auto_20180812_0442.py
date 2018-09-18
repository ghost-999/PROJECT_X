# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-12 04:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evidence', '0005_auto_20180807_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='evidence',
            name='publication_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='evidence',
            name='slug',
            field=models.SlugField(allow_unicode=True, default='defaultslug', unique=True),
            preserve_default=False,
        ),
    ]