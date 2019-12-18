# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-10-14 11:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userApp', '0001_initial'),
        ('marketApp', '0003_axfgoods'),
    ]

    operations = [
        migrations.CreateModel(
            name='AxfCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goodsNum', models.IntegerField()),
                ('is_check', models.BooleanField(default=True)),
                ('c_goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketApp.AxfGoods')),
                ('c_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.AxfUser')),
            ],
            options={
                'db_table': 'axf_cart',
            },
        ),
    ]