# Generated by Django 5.0.1 on 2024-03-06 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zomato', '0007_alter_hotel_rating'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reservation',
        ),
    ]
