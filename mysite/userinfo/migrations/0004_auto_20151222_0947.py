# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0003_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='name',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
