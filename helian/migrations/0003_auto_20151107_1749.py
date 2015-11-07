# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('helian', '0002_auto_20151107_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='powerusage',
            name='device',
            field=models.ForeignKey(to='helian.Device', null=True),
        ),
        migrations.AddField(
            model_name='powerusage',
            name='temperature',
            field=models.FloatField(default=b'0.0'),
        ),
        migrations.AlterField(
            model_name='device',
            name='lastmodified',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 7, 17, 49, 36, 664000)),
        ),
        migrations.AlterField(
            model_name='powerusage',
            name='lastrecorded',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 7, 17, 49, 36, 665000)),
        ),
    ]
