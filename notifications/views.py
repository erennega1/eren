from django.shortcuts import redirect, get_object_or_404
from .models import Notification

def mark_as_read(request, pk):
    if request.user.is_authenticated:
        notification = get_object_or_404(
            Notification, 
            pk=pk, 
            user=request.user
        )
        notification.is_read = True
        notification.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))