# Generated by Django 4.0.6 on 2023-03-30 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_auto_20230330_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(default='images/profile.png', upload_to='images'),
        ),
    ]
