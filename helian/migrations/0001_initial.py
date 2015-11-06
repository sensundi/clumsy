# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('dept', models.ForeignKey(to='helian.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('givenname', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PowerUsage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unitsconsumed', models.FloatField()),
                ('recordedon', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('devicestatus', models.CharField(max_length=100)),
                ('uptime', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='status',
            field=models.ForeignKey(to='helian.Status'),
        ),
        migrations.AddField(
            model_name='device',
            name='usage',
            field=models.ForeignKey(to='helian.PowerUsage'),
        ),
        migrations.AddField(
            model_name='department',
            name='supervisor',
            field=models.ForeignKey(to='helian.Person'),
        ),
    ]
