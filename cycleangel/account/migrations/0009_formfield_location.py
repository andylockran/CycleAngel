# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_formpage_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='formfield',
            name='location',
            field=geoposition.fields.GeopositionField(max_length=42, default=0),
            preserve_default=False,
        ),
    ]
