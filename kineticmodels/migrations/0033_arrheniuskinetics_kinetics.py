# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-17 15:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kineticmodels', '0032_auto_20160617_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='arrheniuskinetics',
            name='kinetics',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='kineticmodels.Kinetics'),
            preserve_default=False,
        ),
    ]
