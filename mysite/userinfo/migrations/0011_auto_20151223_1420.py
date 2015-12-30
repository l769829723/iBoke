# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0010_name_promisewords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='promisewords',
            field=models.CharField(max_length=50, null=True, verbose_name='FirstName'),
        ),
    ]
