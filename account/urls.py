from django.urls import path
from account import views

urlpatterns = [
    path('', views.AccountAPIView.as_view(), name='accounts'),
    path('<int:id>', views.AccountDetailAPIView.as_view(), name='account'),
       
]