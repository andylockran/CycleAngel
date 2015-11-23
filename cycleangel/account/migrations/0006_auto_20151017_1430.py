# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20151017_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountpage',
            old_name='bio',
            new_name='biography',
        ),
    ]
