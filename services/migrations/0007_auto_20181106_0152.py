# Generated by Django 2.1 on 2018-11-05 20:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_auto_20181106_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 11, 5, 20, 7, 4, 555602, tzinfo=utc)),
        ),
    ]
