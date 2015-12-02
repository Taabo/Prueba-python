# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0005_auto_20151202_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='descripcion',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='recompenza',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
