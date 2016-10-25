# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('interest', '0004_auto_20161024_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='genre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='film',
            name='title',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='interest',
            name='film',
            field=models.ForeignKey(to='interest.Film'),
        ),
        migrations.AlterField(
            model_name='interest',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
