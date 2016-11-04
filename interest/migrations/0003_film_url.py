# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interest', '0002_auto_20161102_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='url',
            field=models.URLField(default=''),
        ),
    ]
