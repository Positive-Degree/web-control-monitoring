# Generated by Django 2.1 on 2018-08-08 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0003_auto_20180807_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComputingUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_id', models.CharField(default='', max_length=30)),
                ('unit_name', models.TextField(default='Unit', max_length=30)),
                ('unit_ip_address', models.CharField(default='0.0.0.0', max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='measure_datetime',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='temperature_float',
        ),
        migrations.AddField(
            model_name='sensor',
            name='sensor_id',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='sensor',
            name='sensor_name',
            field=models.TextField(default='Sensor', max_length=30),
        ),
        migrations.AddField(
            model_name='sensor',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='monitoring.db_ComputingUnit'),
        ),
    ]
