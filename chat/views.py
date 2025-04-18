from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def send_message(request):
    if request.method == 'POST':
        recipient_id = request.POST.get('recipient_id')
        text = request.POST.get('text')
        recipient = User.objects.get(id=recipient_id)
        Message.objects.create(sender=request.user, recipient=recipient, text=text)
        return JsonResponse({'status': 'ok'})

@login_required
def get_messages(request, user_id):
    messages = Message.objects.filter(
        models.Q(sender=request.user, recipient_id=user_id) |
        models.Q(sender_id=user_id, recipient=request.user)
    ).order_by('timestamp')
    return JsonResponse({'messages': list(messages.values())})
