from django.contrib.auth.decorators import user_passes_test
from django.urls import path
from .views import (
    chat_room,
    send_message,
    get_messages,
    ChatAdminView
)

urlpatterns = [
    path('', chat_room, name='chat_index'),
    path('user/<int:user_id>/', chat_room, name='chat_with_user'),
    path('ad/<int:ad_id>/', chat_room, name='chat_by_ad'),
    path('send/', send_message, name='send_message'),
    path('get/<int:user_id>/', get_messages, name='get_messages'),
    path('admin/', user_passes_test(lambda u: u.is_superuser)(ChatAdminView.as_view()), name='chat_admin'),
]