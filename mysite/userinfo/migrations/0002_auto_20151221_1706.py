# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='blog_tag',
        ),
        migrations.RemoveField(
            model_name='info',
            name='blog',
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_tags',
            field=models.ManyToManyField(to='userinfo.Tag'),
        ),
        migrations.AddField(
            model_name='info',
            name='blogs',
            field=models.ManyToManyField(to='userinfo.Blog'),
        ),
    ]
