# Generated by Django 2.1 on 2018-08-08 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0006_auto_20180808_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computingunit',
            name='name',
            field=models.CharField(default='Unit', max_length=30),
        ),
    ]
