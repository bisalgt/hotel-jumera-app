# Generated by Django 2.1 on 2018-11-05 13:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0025_auto_20181105_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in',
            field=models.DateField(default=datetime.datetime(2018, 11, 5, 13, 40, 55, 213875, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out',
            field=models.DateField(default=datetime.datetime(2018, 11, 6, 13, 40, 55, 213875, tzinfo=utc)),
        ),
    ]
