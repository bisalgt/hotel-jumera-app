# Generated by Django 2.1 on 2018-11-01 02:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20181101_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 1, 2, 48, 3, 652636, tzinfo=utc)),
        ),
    ]
