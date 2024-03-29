# Generated by Django 5.0 on 2024-02-08 08:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='car_model',
            name='car_description',
            field=models.TextField(default='it is a good car'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='relation_with_car_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.car_model'),
        ),
    ]
