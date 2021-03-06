# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-10-09 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0003_axfmustbuy'),
    ]

    operations = [
        migrations.CreateModel(
            name='AxfMainShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=32)),
                ('trackid', models.IntegerField()),
                ('categoryid', models.IntegerField()),
                ('brandname', models.CharField(max_length=32)),
                ('img1', models.CharField(max_length=256)),
                ('childcid1', models.IntegerField()),
                ('productid1', models.IntegerField()),
                ('longname1', models.CharField(max_length=256)),
                ('price1', models.DecimalField(decimal_places=2, max_digits=9)),
                ('marketprice1', models.DecimalField(decimal_places=2, max_digits=9)),
                ('img2', models.CharField(max_length=256)),
                ('childcid2', models.IntegerField()),
                ('productid2', models.IntegerField()),
                ('longname2', models.CharField(max_length=256)),
                ('price2', models.DecimalField(decimal_places=2, max_digits=9)),
                ('marketprice2', models.DecimalField(decimal_places=2, max_digits=9)),
                ('img3', models.CharField(max_length=256)),
                ('childcid3', models.IntegerField()),
                ('productid3', models.IntegerField()),
                ('longname3', models.CharField(max_length=256)),
                ('price3', models.DecimalField(decimal_places=2, max_digits=9)),
                ('marketprice3', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
            options={
                'db_table': 'axf_mainshow',
            },
        ),
    ]
