# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('genre', models.CharField(max_length=300)),
                ('director', models.CharField(blank=True, max_length=300)),
                ('imdbID', models.CharField(max_length=300, default='empty')),
                ('plot', models.CharField(blank=True, max_length=1000)),
                ('url', models.URLField(blank=True, default='http://')),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('film', models.ForeignKey(to='interest.Film')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
