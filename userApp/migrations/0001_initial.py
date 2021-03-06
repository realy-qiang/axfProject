# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-10-12 03:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AxfUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=128)),
                ('u_password', models.CharField(max_length=256)),
                ('u_emial', models.CharField(max_length=64)),
                ('u_img', models.ImageField(upload_to='icon')),
                ('u_active', models.BooleanField(default=False)),
                ('u_token', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'axf_user',
            },
        ),
    ]
