# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interest', '0006_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='film',
            field=models.ForeignKey(to='interest.Film'),
        ),
    ]
