# Generated by Django 4.2.7 on 2023-11-08 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vintage', '0005_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
    ]