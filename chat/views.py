from django.shortcuts import render, get_object_or_404  
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.db import models 
from .models import Message
from notifications.models import Notification

User = get_user_model()

@login_required
def chat_room(request, user_id=None):
    users = User.objects.exclude(id=request.user.id)
    
    if user_id:
        recipient = get_object_or_404(User, id=user_id)
        messages = Message.objects.filter(
            models.Q(sender=request.user, recipient=recipient) |
            models.Q(sender=recipient, recipient=request.user)
        ).order_by('timestamp')
        return render(request, 'chat/chat.html', {
            'recipient': recipient,
            'messages': messages,
            'users': users
        })
    return render(request, 'chat/index.html', {'users': users})

@csrf_exempt
@login_required
def send_message(request):
    if request.method == 'POST':
        recipient_id = request.POST.get('recipient_id')
        text = request.POST.get('text')
        recipient = User.objects.get(id=recipient_id)
        
        message = Message.objects.create(
            sender=request.user,
            recipient=recipient,
            text=text
        )
        
        Notification.objects.create(
            user=recipient,
            message=f"Новое сообщение от {request.user.username}"
        )
        
        return JsonResponse({'status': 'ok'})

@login_required
def get_messages(request, user_id):
    messages = Message.objects.filter(
        models.Q(sender=request.user, recipient_id=user_id) |
        models.Q(sender_id=user_id, recipient=request.user)
    ).order_by('timestamp')
    
    return JsonResponse({
        'messages': [
            {
                'text': msg.text,
                'sender': msg.sender.username,
                'time': msg.timestamp.strftime("%H:%M")
            } 
            for msg in messages
        ]
    })