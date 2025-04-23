from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.chat_room, name='index'),
    path('ad/<int:ad_id>/', views.chat_room, name='room_by_ad'),  
    path('<int:user_id>/', views.chat_room, name='room'),  
    path('send/', views.send_message, name='send_message'),
    path('get/<int:user_id>/', views.get_messages, name='get_messages'),
]