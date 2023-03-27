# Generated by Django 3.0.2 on 2021-03-15 12:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='status',
        ),
        migrations.AddField(
            model_name='booking',
            name='ordered_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered')], default='pending', max_length=30),
        ),
    ]