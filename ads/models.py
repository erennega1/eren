from django.db import models
from django.contrib.auth.models import User  

class Ad(models.Model):
    CATEGORY_CHOICES = [
        ('electronics', 'Электроника'),
        ('vehicles', 'Транспорт'),
        ('real_estate', 'Недвижимость'),
        ('clothing', 'Одежда'),
        ('other', 'Другое'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='ads/', blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')

    def __str__(self):
        return self.title
