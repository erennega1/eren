# Generated by Django 5.1.7 on 2025-04-18 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['-created_at'], 'verbose_name': 'Уведомление', 'verbose_name_plural': 'Уведомления'},
        ),
    ]
