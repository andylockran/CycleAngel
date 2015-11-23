# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20151017_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='formpage',
            name='location',
            field=geoposition.fields.GeopositionField(default=0, max_length=42),
            preserve_default=False,
        ),
    ]
