from django.urls import path
from . import views
from .views import add_review

urlpatterns = [
     path('ads/<int:ad_id>/review/', add_review, name='add_review'),
     path('review/<int:review_id>/delete/', views.delete_review, name='delete_review'),
]