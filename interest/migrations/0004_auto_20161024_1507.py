# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interest', '0003_auto_20161024_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='film',
            field=models.ForeignKey(null=True, blank=True, to='interest.Film'),
        ),
    ]
