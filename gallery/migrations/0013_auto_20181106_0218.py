# Generated by Django 2.1 on 2018-11-05 20:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0012_auto_20181106_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryuploads',
            name='upload_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
