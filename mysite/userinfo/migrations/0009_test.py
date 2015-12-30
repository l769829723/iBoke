# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0008_auto_20151222_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kindof', models.CharField(max_length=50, verbose_name='KindOf')),
                ('tags', models.ManyToManyField(to='userinfo.Tag')),
            ],
        ),
    ]
