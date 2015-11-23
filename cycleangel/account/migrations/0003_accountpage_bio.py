# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20151011_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountpage',
            name='bio',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
