# Generated by Django 5.0 on 2024-02-08 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_car_model_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car_model',
            name='quantity',
            field=models.IntegerField(default=5),
        ),
    ]
