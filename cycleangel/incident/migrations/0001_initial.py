# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailcore', '0019_verbose_names_cleanup'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncidentPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, serialize=False, primary_key=True, to='wagtailcore.Page')),
                ('time', models.DateTimeField()),
                ('location', geoposition.fields.GeopositionField(max_length=42)),
                ('message', models.TextField(max_length=400)),
                ('assignee', models.ForeignKey(related_name='assignee', to=settings.AUTH_USER_MODEL)),
                ('reporter', models.ForeignKey(related_name='reporter', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
