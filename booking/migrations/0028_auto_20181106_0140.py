# Generated by Django 2.1 on 2018-11-05 19:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0027_auto_20181106_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in',
            field=models.DateField(default=datetime.datetime(2018, 11, 5, 19, 55, 45, 516172, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out',
            field=models.DateField(default=datetime.datetime(2018, 11, 6, 19, 55, 45, 516172, tzinfo=utc)),
        ),
    ]
