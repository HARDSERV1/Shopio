# Generated by Django 2.2.2 on 2020-01-30 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200130_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='current_price',
            field=models.FloatField(default=0, verbose_name='Current price'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='old_price',
            field=models.FloatField(default=0, verbose_name='Old Price'),
        ),
    ]
