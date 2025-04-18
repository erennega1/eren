from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('mark-as-read/<int:pk>/', views.mark_as_read, name='mark_as_read'),
]