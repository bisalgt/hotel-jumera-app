# Generated by Django 2.1 on 2018-11-04 03:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0023_auto_20181103_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in',
            field=models.DateField(default=datetime.datetime(2018, 11, 4, 3, 24, 0, 502260, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out',
            field=models.DateField(default=datetime.datetime(2018, 11, 5, 3, 24, 0, 502260, tzinfo=utc)),
        ),
    ]