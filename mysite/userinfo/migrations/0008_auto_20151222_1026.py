# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0007_auto_20151222_1021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
