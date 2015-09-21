# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='first_name',
            field=models.CharField(default=b'Sujit', max_length=50),
        ),
        migrations.AddField(
            model_name='users',
            name='last_name',
            field=models.CharField(default=b'Mahavarkar', max_length=50),
        ),
    ]
