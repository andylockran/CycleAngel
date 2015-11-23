# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20151017_1648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formfield',
            name='page',
        ),
        migrations.AddField(
            model_name='locationfield',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='form_fields', default=0, to='account.FormPage'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='FormField',
        ),
    ]
