# Generated by Django 5.0 on 2024-02-08 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_comments_model_delete_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='car_model',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
