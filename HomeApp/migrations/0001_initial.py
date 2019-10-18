# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-10-09 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainShow',
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
                ('longname1', models.CharField(max_length=128)),
                ('price1', models.FloatField()),
                ('marketprice1', models.FloatField()),
                ('img2', models.CharField(max_length=256)),
                ('childcid2', models.IntegerField()),
                ('productid2', models.IntegerField()),
                ('longname2', models.CharField(max_length=128)),
                ('price2', models.FloatField()),
                ('marketprice2', models.FloatField()),
                ('img3', models.CharField(max_length=256)),
                ('childcid3', models.IntegerField()),
                ('productid3', models.IntegerField()),
                ('longname3', models.CharField(max_length=128)),
                ('price3', models.FloatField()),
                ('marketprice3', models.FloatField()),
            ],
            options={
                'db_table': 'axf_mainshow',
            },
        ),
        migrations.CreateModel(
            name='MustBuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=32)),
                ('trackid', models.IntegerField()),
            ],
            options={
                'db_table': 'axf_mustbuy',
            },
        ),
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=32)),
                ('trackid', models.IntegerField()),
            ],
            options={
                'db_table': 'axf_nav',
            },
        ),
        migrations.CreateModel(
            name='Wheel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=32)),
                ('trackid', models.IntegerField()),
            ],
            options={
                'db_table': 'axf_wheel',
            },
        ),
    ]