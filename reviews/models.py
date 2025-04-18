from django.db import models
from django.conf import settings
from ads.models import Ad  

class Review(models.Model):
    RATING_CHOICES = [
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'), 
        (4, '★★★★☆'),
        (5, '★★★★★')
    ]
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, 
                             related_name='reviews_given',
                             on_delete=models.CASCADE)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL,
                                related_name='reviews_received',
                                on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE,
                         related_name='reviews')
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)  

    class Meta:
        unique_together = ('author', 'ad')  

    def __str__(self):
        return f"Отзыв {self.id} для {self.recipient.username}"