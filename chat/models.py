from django.db import models
from django.conf import settings
from django.utils import timezone

class Message(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sent_messages'
    )
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='received_messages'
    )
    text = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)
    ad = models.ForeignKey(
        'ads.Ad',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='messages'
    )

    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['sender', 'recipient']),
            models.Index(fields=['timestamp']),
        ]

    def __str__(self):
        return f"{self.sender} → {self.recipient}: {self.text[:20]}..."
