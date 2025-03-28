from django.urls import path
from .views import ad_list, ad_detail  # Убедись, что импортируешь функции правильно

urlpatterns = [
    path('', ad_list, name='ad_list'),  # Главная страница объявлений
    path('<int:ad_id>/', ad_detail, name='ad_detail'),  # Детальная страница объявления
]