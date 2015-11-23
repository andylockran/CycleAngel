# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailsearchpromotions', '0001_initial'),
        ('wagtailforms', '0002_add_verbose_names'),
        ('wagtailcore', '0019_verbose_names_cleanup'),
        ('wagtailredirects', '0002_add_verbose_names'),
        ('account', '0004_auto_20151017_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formfield',
            name='page',
        ),
        migrations.RemoveField(
            model_name='formpage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='FormField',
        ),
        migrations.DeleteModel(
            name='FormPage',
        ),
    ]
