# Generated by Django 5.0 on 2024-02-10 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_purchase_purchased_car_brand_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='who_purchased_user_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]