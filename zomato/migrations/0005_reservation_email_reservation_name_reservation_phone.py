# Generated by Django 5.0.1 on 2024-03-06 22:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zomato', '0004_room_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AddField(
            model_name='reservation',
            name='name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='reservation',
            name='phone',
            field=models.IntegerField(default=None, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(15)]),
        ),
    ]
