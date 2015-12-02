# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota_perdida', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mascota_perdida',
            name='perdido',
        ),
        migrations.AddField(
            model_name='mascota_perdida',
            name='direccion',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mascota_perdida',
            name='sector',
            field=models.CharField(max_length=40, blank=True),
        ),
    ]
