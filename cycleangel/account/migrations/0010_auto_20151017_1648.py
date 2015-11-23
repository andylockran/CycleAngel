# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_formfield_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationField',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('label', models.CharField(max_length=255, verbose_name='Label', help_text='The label of the form field')),
                ('field_type', models.CharField(max_length=16, verbose_name='Field type', choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time')])),
                ('required', models.BooleanField(verbose_name='Required', default=True)),
                ('choices', models.CharField(blank=True, max_length=512, verbose_name='Choices', help_text='Comma separated list of choices. Only applicable in checkboxes, radio and dropdown.')),
                ('default_value', models.CharField(blank=True, max_length=255, verbose_name='Default value', help_text='Default value. Comma separated values supported for checkboxes.')),
                ('help_text', models.CharField(blank=True, max_length=255, verbose_name='Help text')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='formfield',
            name='location',
        ),
        migrations.RemoveField(
            model_name='formpage',
            name='location',
        ),
    ]
