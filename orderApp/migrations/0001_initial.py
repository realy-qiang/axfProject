# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-10-16 06:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('marketApp', '0003_axfgoods'),
        ('userApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AxfAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=256)),
                ('tel', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'axf_address',
            },
        ),
        migrations.CreateModel(
            name='AxfOderAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oa_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orderApp.AxfAddress')),
            ],
            options={
                'db_table': 'axf_orderaddress',
            },
        ),
        migrations.CreateModel(
            name='AxfOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_time', models.DateTimeField(auto_now_add=True)),
                ('o_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.AxfUser')),
            ],
            options={
                'db_table': 'axf_order',
            },
        ),
        migrations.CreateModel(
            name='AxfOrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goodNum', models.IntegerField()),
                ('goodTotal', models.FloatField()),
                ('og_goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketApp.AxfGoods')),
                ('og_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orderApp.AxfOrder')),
            ],
            options={
                'db_table': 'axf_ordergoods',
            },
        ),
        migrations.AddField(
            model_name='axfoderaddress',
            name='oa_order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orderApp.AxfOrder'),
        ),
    ]
