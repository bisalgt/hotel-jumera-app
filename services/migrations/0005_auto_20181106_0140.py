# Generated by Django 2.1 on 2018-11-05 19:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20181106_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 11, 5, 19, 55, 45, 438051, tzinfo=utc)),
        ),
    ]
