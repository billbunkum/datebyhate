# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interest', '0007_auto_20161025_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='director',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='genre',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='film',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
