from django.db import models

class Ad(models.Model):
    title = models.CharField(max_length=255)  # Заголовок объявления
    description = models.TextField()  # Описание
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания

    def __str__(self):
        return self.title  
