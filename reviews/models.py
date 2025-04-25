from django.db import models
from django.contrib.auth import get_user_model
from ads.models import Ad

User = get_user_model()

class Review(models.Model):
    RATING_CHOICES = [
        (1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), 
        (4, '★★★★☆'), (5, '★★★★★')
    ]
    
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='ad_reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f"Отзыв на {self.ad.title} от {self.author.username}"