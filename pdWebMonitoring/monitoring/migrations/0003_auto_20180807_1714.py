# Generated by Django 2.1 on 2018-08-07 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0002_temperature_temperature_float'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Temperature',
            new_name='Sensor',
        ),
    ]
