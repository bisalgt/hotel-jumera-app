# Generated by Django 2.1 on 2018-11-03 18:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0022_auto_20181103_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in',
            field=models.DateField(default=datetime.datetime(2018, 11, 3, 18, 13, 9, 351105, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out',
            field=models.DateField(default=datetime.datetime(2018, 11, 4, 18, 13, 9, 351105, tzinfo=utc)),
        ),
    ]