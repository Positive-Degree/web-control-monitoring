# Generated by Django 2.1 on 2018-08-14 22:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0015_auto_20180814_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='computingunit',
            name='ping_frequency',
            field=models.PositiveIntegerField(default=60, validators=[django.core.validators.MaxValueValidator(1800)]),
        ),
        migrations.AlterField(
            model_name='computingunit',
            name='port_number',
            field=models.PositiveIntegerField(default=2000, validators=[django.core.validators.MaxValueValidator(99999)]),
        ),
    ]
