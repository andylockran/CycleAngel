# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20151017_1651'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LocationField',
            new_name='FormField',
        ),
    ]
