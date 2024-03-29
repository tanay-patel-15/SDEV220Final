# Generated by Django 5.0.1 on 2024-03-06 23:25

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zomato', '0008_delete_reservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
                ('phone', models.IntegerField(default=None, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(15)])),
                ('email', models.EmailField(default=None, max_length=254)),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zomato.hotel')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zomato.roomtype')),
            ],
        ),
    ]
