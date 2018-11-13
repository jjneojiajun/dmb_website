# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-11-12 04:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_rates', '0002_auto_20181112_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankrates',
            name='bank_image',
            field=models.CharField(choices=[('http://127.0.0.1:8000/media/bank_images/dbs_logo.jpg', 'DBS'), ('http://127.0.0.1:8000/media/bank_images/uob_logo.png', 'UOB'), ('http://127.0.0.1:8000/media/bank_images/uob_logo.png', 'Standard Charter'), ('http://127.0.0.1:8000/media/bank_images/maybank_logo.png', 'Maybank'), ('http://127.0.0.1:8000/media/bank_images/hong_leong.jpg', 'Hong Leong Finance'), ('http://127.0.0.1:8000/media/bank_images/bea_logo.png', 'BEA'), ('http://127.0.0.1:8000/media/bank_images/ocbc_logo.png', 'OCBC'), ('http://127.0.0.1:8000/media/bank_images/posb_logo.png', 'POSB'), ('http://127.0.0.1:8000/media/bank_images/rhb_logo.png', 'RHB')], default='', max_length=200),
        ),
    ]
