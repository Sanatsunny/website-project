# Generated by Django 4.2.7 on 2023-11-08 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vintage', '0006_profile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.IntegerField(default='1234567890'),
        ),
    ]
