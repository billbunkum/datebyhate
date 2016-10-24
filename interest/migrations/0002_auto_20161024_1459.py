# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='title_id',
        ),
        migrations.AddField(
            model_name='film',
            name='director',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='film',
            name='title',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
