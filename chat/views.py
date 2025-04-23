from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model
from django.db.models import Q, Max
from django.db import models
from .models import Message
from notifications.models import Notification
from ads.models import Ad

User = get_user_model()

def get_recent_chats(user):
    
    last_messages = Message.objects.filter(
        Q(sender=user) | Q(recipient=user)
    ).values('sender', 'recipient').annotate(
        last_msg=Max('timestamp')
    )
    
    recent_chats = []
    for msg in last_messages:
        other_user_id = msg['sender'] if msg['sender'] != user.id else msg['recipient']
        try:
            other_user = User.objects.get(id=other_user_id)
            last_message = Message.objects.filter(
                Q(sender=user, recipient=other_user) |
                Q(sender=other_user, recipient=user)
            ).latest('timestamp')
            
            recent_chats.append({
                'user': other_user,
                'last_message': last_message,
                'unread_count': Message.objects.filter(
                    sender=other_user,
                    recipient=user,
                    is_read=False
                ).count()
            })
        except User.DoesNotExist:
            continue
    
    return sorted(recent_chats, key=lambda x: x['last_message'].timestamp, reverse=True)

@login_required
def chat_room(request, user_id=None, ad_id=None):

    users = User.objects.exclude(id=request.user.id)
    current_ad = None
    
    if ad_id:
        current_ad = get_object_or_404(Ad, id=ad_id)
        recipient = current_ad.user
        user_id = recipient.id
    
    if user_id:
        recipient = get_object_or_404(User, id=user_id)
        messages = Message.objects.filter(
            Q(sender=request.user, recipient=recipient) |
            Q(sender=recipient, recipient=request.user)
        ).order_by('timestamp')
        
       
        Message.objects.filter(
            sender=recipient,
            recipient=request.user,
            is_read=False
        ).update(is_read=True)
        
        return render(request, 'chat/chat.html', {
            'recipient': recipient,
            'messages': messages,
            'users': users,
            'current_ad': current_ad
        })
    
    return render(request, 'chat/room.html', {
        'users': users,
        'recent_messages': get_recent_chats(request.user)
    })

@login_required
@require_POST
def send_message(request):
    recipient_id = request.POST.get('recipient_id')
    ad_id = request.POST.get('ad_id')
    text = request.POST.get('text', '').strip()
    
    if not text:
        return JsonResponse({'status': 'error', 'message': 'Сообщение не может быть пустым'})
    
    recipient = get_object_or_404(User, id=recipient_id)
    ad = get_object_or_404(Ad, id=ad_id) if ad_id else None
    
    message = Message.objects.create(
        sender=request.user,
        recipient=recipient,
        text=text,
        ad=ad
    )
    
    Notification.objects.create(
        user=recipient,
        message=f"Новое сообщение от {request.user.username}",
        notification_type='message'
    )
    
    return JsonResponse({
        'status': 'ok',
        'message': {
            'text': message.text,
            'sender': message.sender.username,
            'time': message.timestamp.strftime("%H:%M"),
            'is_read': message.is_read
        }
    })

@login_required
def get_messages(request, user_id):
    messages = Message.objects.filter(
        Q(sender=request.user, recipient_id=user_id) |
        Q(sender_id=user_id, recipient=request.user)
    ).order_by('timestamp')
    
    return JsonResponse({
        'messages': [
            {
                'id': msg.id,
                'text': msg.text,
                'sender': msg.sender.username,
                'time': msg.timestamp.strftime("%H:%M"),
                'is_read': msg.is_read
            } 
            for msg in messages
        ]
    })