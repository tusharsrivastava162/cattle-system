# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 13:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20170630_0413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 5, 18, 37, 10, 122008)),
        ),
        migrations.AlterField(
            model_name='post',
            name='last_modified_on',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 5, 18, 37, 10, 122086)),
        ),
    ]
