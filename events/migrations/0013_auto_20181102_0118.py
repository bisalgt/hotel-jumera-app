# Generated by Django 2.1 on 2018-11-01 19:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20181101_1027'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['time']},
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 1, 19, 33, 59, 224719, tzinfo=utc)),
        ),
    ]
