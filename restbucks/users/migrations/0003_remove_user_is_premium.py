# Generated by Django 3.0.6 on 2020-06-01 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_is_mobile_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_premium',
        ),
    ]