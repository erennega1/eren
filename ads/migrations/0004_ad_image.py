# Generated by Django 5.1.7 on 2025-04-04 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_remove_ad_created_at_alter_ad_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ads/'),
        ),
    ]
