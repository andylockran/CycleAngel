# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('incident', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidentpage',
            name='assignee',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, related_name='assignee', on_delete=django.db.models.deletion.SET_NULL),
        ),
        migrations.AlterField(
            model_name='incidentpage',
            name='reporter',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, related_name='reporter', on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
