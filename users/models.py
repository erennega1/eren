from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File
import os

def create_default_avatar():
    """Создает изображение аватара по умолчанию"""
    img = Image.new('RGB', (200, 200), color=(73, 109, 137))
    d = ImageDraw.Draw(img)
    d.text((20, 100), "AVATAR", fill=(255, 255, 255))
    
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    return File(buffer, name='default.png')

class Profile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='profile'
    )
    avatar = models.ImageField(
        upload_to='avatars/', 
        default='avatars/default.png'
    )
    bio = models.TextField(blank=True, default='')
    phone = models.CharField(max_length=20, blank=True)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return f'Профиль {self.user.username}'

    def save(self, *args, **kwargs):
        if not self.avatar:
            self.avatar.save('default.png', create_default_avatar(), save=False)
        super().save(*args, **kwargs)

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()