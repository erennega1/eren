from django.urls import path
from .views import send_message, get_messages

urlpatterns = [
    path('send/', send_message, name='send_message'),
    path('get/<int:user_id>/', get_messages, name='get_messages'),
]