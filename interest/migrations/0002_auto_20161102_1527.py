# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interest',
            name='has_hate',
        ),
        migrations.AddField(
            model_name='film',
            name='imdbID',
            field=models.CharField(default='empty', max_length=300),
        ),
        migrations.AddField(
            model_name='film',
            name='plot',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
