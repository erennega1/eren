# Generated by Django 5.1.7 on 2025-04-18 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0011_remove_profile_description_profile_bio'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
