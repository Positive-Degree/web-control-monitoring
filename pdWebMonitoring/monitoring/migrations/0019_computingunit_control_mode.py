# Generated by Django 2.1 on 2018-08-30 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0018_sensor_temperature'),
    ]

    operations = [
        migrations.AddField(
            model_name='computingunit',
            name='control_mode',
            field=models.CharField(choices=[('auto', 'Autonomous'), ('manual', 'Manual')], default='autonomous', max_length=10),
        ),
    ]
