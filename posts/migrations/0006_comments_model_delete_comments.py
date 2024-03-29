# Generated by Django 5.0 on 2024-02-08 18:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_car_model_car_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_one', models.DateTimeField(auto_now_add=True)),
                ('relation_with_car_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.car_model')),
            ],
        ),
        migrations.DeleteModel(
            name='comments',
        ),
    ]
