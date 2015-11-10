# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raza', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mascota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('color', models.CharField(max_length=20, blank=True)),
                ('sexo', models.CharField(max_length=20, blank=True)),
                ('descripcion', models.TextField(null=True)),
                ('raza', models.ForeignKey(to='raza.raza')),
            ],
        ),
    ]
