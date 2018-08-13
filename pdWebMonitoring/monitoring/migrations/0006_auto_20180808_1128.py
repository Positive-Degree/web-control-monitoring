# Generated by Django 2.1 on 2018-08-08 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0005_auto_20180808_1107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='computingunit',
            old_name='unit_ip_address',
            new_name='ip_address',
        ),
        migrations.RenameField(
            model_name='computingunit',
            old_name='unit_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='sensor',
            old_name='sensor_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='computingunit',
            name='running_process',
            field=models.CharField(default='mining', max_length=30),
        ),
    ]