# Generated by Django 2.1 on 2018-10-31 08:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20181030_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 31, 8, 10, 8, 265747, tzinfo=utc)),
        ),
    ]
