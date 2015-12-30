# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validation', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=80, verbose_name='BlogTitle')),
                ('blog_body', models.TextField(max_length=5000, verbose_name='BlogBody')),
                ('blog_read_count', models.IntegerField(default=0, null=True, verbose_name='BlogReadCount')),
                ('blog_votes', models.IntegerField(default=0, null=True, verbose_name='BlogVotes')),
                ('blog_publish_date', models.DateTimeField(auto_now_add=True, verbose_name='BlogPublishDate')),
                ('blog_modify_date', models.DateTimeField(auto_now=True, verbose_name='BlogPublishDate')),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.ForeignKey(null=True, to='userinfo.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(max_length=50, null=True, verbose_name='LastName')),
                ('firstname', models.CharField(max_length=50, null=True, verbose_name='FirstName')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='TagName')),
            ],
        ),
        migrations.AddField(
            model_name='info',
            name='name',
            field=models.ForeignKey(null=True, to='userinfo.Name'),
        ),
        migrations.AddField(
            model_name='info',
            name='user',
            field=models.ForeignKey(null=True, to='validation.UserAuth'),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_tag',
            field=models.ForeignKey(null=True, to='userinfo.Tag'),
        ),
    ]
