# Generated by Django 2.1 on 2018-08-09 19:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0010_auto_20180809_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computingunit',
            name='id',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='id',
        ),
        migrations.AlterField(
            model_name='computingunit',
            name='port_number',
            field=models.PositiveIntegerField(default=2000, max_length=4, validators=[django.core.validators.MaxValueValidator(9999)]),
        ),
        migrations.AlterField(
            model_name='computingunit',
            name='unit_id',
            field=models.CharField(default='', max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='sensor_id',
            field=models.CharField(default='', max_length=30, primary_key=True, serialize=False),
        ),
    ]
