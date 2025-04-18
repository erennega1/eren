from django.shortcuts import get_object_or_404, redirect
from .models import Notification

def mark_as_read(request, pk):
    if request.user.is_authenticated:
        notification = get_object_or_404(Notification, pk=pk, user=request.user)
        notification.is_read = True
        notification.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))