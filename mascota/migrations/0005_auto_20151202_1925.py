# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0004_auto_20151110_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='color',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='descripcion',
            field=models.TextField(default=1, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mascota',
            name='perdido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='recompenza',
            field=models.IntegerField(default=1, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mascota',
            name='sexo',
            field=models.CharField(max_length=20),
        ),
    ]
