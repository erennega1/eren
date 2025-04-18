from django import template
from notifications.models import Notification

register = template.Library()

@register.filter
def unread_notifications(user):
    return Notification.objects.filter(user=user, is_read=False)