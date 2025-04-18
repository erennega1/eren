from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.template.loader import render_to_string
from .models import Review

@receiver(post_save, sender=Review)
def send_review_notification(sender, instance, created, **kwargs):
    if created:
        subject = f'Новый отзыв на ваше объявление "{instance.ad.title}"'
        message = render_to_string('emails/new_review.html', {
            'recipient': instance.recipient,
            'author': instance.author,
            'ad': instance.ad,
            'review': instance
        })
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [instance.recipient.email],
            html_message=message,
            fail_silently=True
        )