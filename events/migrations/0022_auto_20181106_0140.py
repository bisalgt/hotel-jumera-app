# Generated by Django 2.1 on 2018-11-05 19:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0021_auto_20181106_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='futureevent',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 5, 19, 55, 45, 500548, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pastevent',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 5, 19, 55, 45, 500548, tzinfo=utc)),
        ),
    ]
