# Generated by Django 4.1 on 2022-09-23 15:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_remove_furniture_upload_remove_furniture_url_img_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='furniture',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 23, 17, 51, 42, 479567)),
        ),
    ]
