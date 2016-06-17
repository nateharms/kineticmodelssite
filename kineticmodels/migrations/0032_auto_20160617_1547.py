# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-17 15:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kineticmodels', '0031_auto_20160617_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kinetics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rkPrimeID', models.CharField(blank=True, max_length=10)),
                ('is_reverse', models.BooleanField(default=False, help_text=b'Is this the rate for the reverse reaction?')),
                ('reaction', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='kineticmodels.Reaction')),
                ('source', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kineticmodels.Source')),
            ],
            options={
                'verbose_name_plural': 'Kinetics',
            },
        ),
        migrations.RemoveField(
            model_name='arrheniuskinetics',
            name='is_reverse',
        ),
        migrations.RemoveField(
            model_name='arrheniuskinetics',
            name='reaction',
        ),
        migrations.RemoveField(
            model_name='arrheniuskinetics',
            name='rkPrimeID',
        ),
        migrations.RemoveField(
            model_name='arrheniuskinetics',
            name='source',
        ),
    ]