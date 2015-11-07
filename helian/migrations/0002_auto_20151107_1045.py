# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('helian', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='usage',
        ),
        migrations.RemoveField(
            model_name='powerusage',
            name='recordedon',
        ),
        migrations.RemoveField(
            model_name='status',
            name='devicestatus',
        ),
        migrations.RemoveField(
            model_name='status',
            name='uptime',
        ),
        migrations.AddField(
            model_name='device',
            name='lastmodified',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 7, 10, 45, 35, 15000)),
        ),
        migrations.AddField(
            model_name='device',
            name='owner',
            field=models.ForeignKey(to='helian.Person', null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.CharField(default=b'unspecified@sitebrain.com', max_length=50),
        ),
        migrations.AddField(
            model_name='powerusage',
            name='lastrecorded',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 7, 10, 45, 35, 16000)),
        ),
        migrations.AddField(
            model_name='status',
            name='name',
            field=models.CharField(default=b'unspecified', max_length=20),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(default=b'unspecified', max_length=20),
        ),
        migrations.AlterField(
            model_name='device',
            name='dept',
            field=models.ForeignKey(to='helian.Department', null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='name',
            field=models.CharField(default=b'unspecified', max_length=20),
        ),
        migrations.AlterField(
            model_name='device',
            name='status',
            field=models.ForeignKey(to='helian.Status', null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='givenname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(default=b'unspecified', max_length=20),
        ),
        migrations.AlterField(
            model_name='person',
            name='surname',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
