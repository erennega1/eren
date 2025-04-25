from django.db import models
from django.conf import settings
from django.utils import timezone

class Message(models.Model):
 
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sent_messages',
        verbose_name='Отправитель'
    )
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='received_messages',
        verbose_name='Получатель'
    )
    text = models.TextField(verbose_name='Текст сообщения')
    timestamp = models.DateTimeField(
        default=timezone.now,
        verbose_name='Время отправки'
    )
    is_read = models.BooleanField(
        default=False,
        verbose_name='Прочитано'
    )
    ad = models.ForeignKey(
        'ads.Ad',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='messages',
        verbose_name='Связанное объявление'
    )

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['sender', 'recipient']),
            models.Index(fields=['timestamp']),
            models.Index(fields=['is_read']),
        ]

    def __str__(self):
        return f"Сообщение от {self.sender} к {self.recipient} ({self.timestamp})"

    def mark_as_read(self):
        
        if not self.is_read:
            self.is_read = True
            self.save()
