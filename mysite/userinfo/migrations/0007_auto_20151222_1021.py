# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0006_test_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='name',
            new_name='kindof',
        ),
    ]
