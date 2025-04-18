from django.urls import path
from .views import mark_as_read
app_name = 'notifications'
urlpatterns = [
    path('mark-as-read/<int:notification_id>/', mark_as_read, name='mark_as_read'),
]