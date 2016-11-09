# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interest', '0008_auto_20161109_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='social_link',
            field=models.CharField(blank=True, null=True, max_length=30),
        ),
    ]
