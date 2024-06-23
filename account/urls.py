from django.urls import path
from account import views

urlpatterns = [
    path('create', views.CreateAccountAPIView.as_view(), name='create-account'),
    path('list', views.AccountListAPIView.as_view(), name='list-accounts'),
    
]