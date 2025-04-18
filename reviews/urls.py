from django.urls import path
from .views import add_review

urlpatterns = [
    path('ad/<int:ad_id>/review/', add_review, name='add_review'),
]