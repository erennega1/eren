from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_room, name='chat_index'),
    path('user/<int:user_id>/', views.chat_room, name='chat_with_user'),
    path('ad/<int:ad_id>/', views.chat_room, name='chat_by_ad'),
    path('send/', views.send_message, name='send_message'),
    path('get/<int:user_id>/', views.get_messages, name='get_messages'),
]