# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAuth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(default=1000, verbose_name='User_id')),
                ('username', models.CharField(max_length=50, verbose_name='Username')),
                ('password', models.CharField(max_length=50, verbose_name='Password')),
            ],
        ),
    ]
