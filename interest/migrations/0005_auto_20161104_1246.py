# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interest', '0004_auto_20161104_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='url',
            field=models.URLField(blank=True, default='http://'),
        ),
    ]
