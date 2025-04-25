from django.urls import path
from . import views

urlpatterns = [
    path('', views.ad_list, name='ad_list'),
    path('create/', views.ad_create, name='ad_create'),
    path('<int:ad_id>/', views.ad_detail, name='ad_detail'),
    path('<int:ad_id>/edit/', views.ad_edit, name='ad_edit'),
    path('<int:ad_id>/delete/', views.ad_delete, name='ad_delete'),
    path('my-ads/', views.my_ads, name='my_ads'),
    path('favorites/', views.favorite_ads, name='favorites'),
    path('<int:ad_id>/favorite/', views.toggle_favorite, name='toggle_favorite'),
]