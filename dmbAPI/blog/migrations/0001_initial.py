# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-11-12 00:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogPosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=109)),
                ('content', models.TextField(default='', max_length=10000)),
            ],
        ),
    ]
