# Generated by Django 2.2.2 on 2020-01-31 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20200131_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/', verbose_name='image'),
        ),
    ]
