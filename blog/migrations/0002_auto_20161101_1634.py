# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 14:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2016, 11, 1, 14, 34, 38, 361471, tzinfo=utc))),
                ('approved_comment', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2016, 11, 1, 14, 34, 38, 361471, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coments', to='blog.Post'),
        ),
    ]
