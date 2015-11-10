# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
        ('mascota', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='dueno',
            field=models.ForeignKey(default=2, to='usuario.usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mascota',
            name='perdido',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mascota',
            name='recompenza',
            field=models.IntegerField(null=True),
        ),
    ]
