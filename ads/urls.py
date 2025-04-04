from django.urls import path
from .views import ad_list, ad_detail

urlpatterns = [
    path('', ad_list, name='ad_list'),  
    path('<int:ad_id>/', ad_detail, name='ad_detail'),  
]