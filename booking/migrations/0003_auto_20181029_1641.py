# Generated by Django 2.1 on 2018-10-29 10:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20181029_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in',
            field=models.DateField(default=datetime.datetime(2018, 10, 29, 16, 41, 12, 670618)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out',
            field=models.DateField(default=datetime.datetime(2018, 10, 30, 16, 41, 12, 670618)),
        ),
    ]
