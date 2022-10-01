# Generated by Django 4.1 on 2022-09-30 17:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_alter_furniture_date_furnitureimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furniture',
            name='caracteristic',
            field=models.CharField(max_length=255, verbose_name='caractéristiques : massif plaque // marqueterie sculpture boite_et_coffret jeux meuble_a_secret'),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='category',
            field=models.CharField(max_length=42, verbose_name='catégorie : creation/restauration'),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 30, 19, 26, 36, 632255)),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='image_liste (plutot carré)'),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='keywords',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='mots clé à afficher en plus de catgorie et caractérisitique'),
        ),
        migrations.AlterField(
            model_name='furnitureimage',
            name='images',
            field=models.FileField(upload_to='', verbose_name='Images item plutot rectangulaire'),
        ),
    ]