# Generated by Django 2.1 on 2018-11-01 01:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20181031_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 1, 1, 22, 36, 439243, tzinfo=utc)),
        ),
    ]
