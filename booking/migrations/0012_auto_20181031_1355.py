# Generated by Django 2.1 on 2018-10-31 08:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0011_auto_20181030_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in',
            field=models.DateField(default=datetime.datetime(2018, 10, 31, 13, 55, 8, 280738)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out',
            field=models.DateField(default=datetime.datetime(2018, 11, 1, 13, 55, 8, 280738)),
        ),
    ]
