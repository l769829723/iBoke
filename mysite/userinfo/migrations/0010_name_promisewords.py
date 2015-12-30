# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0009_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='name',
            name='promisewords',
            field=models.CharField(max_length=15, null=True, verbose_name='FirstName'),
        ),
    ]
