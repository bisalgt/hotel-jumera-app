# Generated by Django 2.1 on 2018-11-01 01:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0013_auto_20181101_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in',
            field=models.DateField(default=datetime.datetime(2018, 11, 1, 1, 32, 35, 978153, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out',
            field=models.DateField(default=datetime.datetime(2018, 11, 2, 1, 32, 35, 978153, tzinfo=utc)),
        ),
    ]
