# Generated by Django 4.0.6 on 2023-03-30 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_remove_customer_addres_s_remove_customer_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]






