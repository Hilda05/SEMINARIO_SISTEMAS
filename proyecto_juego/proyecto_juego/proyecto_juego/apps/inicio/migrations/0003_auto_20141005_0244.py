# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_empleado'),
    ]

    operations = [
        migrations.DeleteModel(
            name='empleado',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Password',
            field=models.CharField(max_length=20),
        ),
    ]
