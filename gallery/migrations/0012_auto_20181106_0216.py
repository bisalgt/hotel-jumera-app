# Generated by Django 2.1 on 2018-11-05 20:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0011_auto_20181106_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryuploads',
            name='upload_date',
            field=models.DateField(default=datetime.datetime(2018, 11, 5, 20, 31, 22, 461320, tzinfo=utc)),
        ),
    ]
