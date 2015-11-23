# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailsearchpromotions', '0001_initial'),
        ('wagtailcore', '0020_add_index_on_page_first_published_at'),
        ('wagtailredirects', '0004_set_unique_on_path_and_site'),
        ('wagtailforms', '0002_add_verbose_names'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('incident', '0002_auto_20151123_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('time', models.DateTimeField()),
                ('location', geoposition.fields.GeopositionField(max_length=42)),
                ('message', models.TextField(max_length=400)),
                ('assignee', models.ForeignKey(related_name='assignee', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
                ('reporter', models.ForeignKey(related_name='reporter', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='incidentpage',
            name='assignee',
        ),
        migrations.RemoveField(
            model_name='incidentpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='incidentpage',
            name='reporter',
        ),
        migrations.DeleteModel(
            name='IncidentPage',
        ),
    ]
