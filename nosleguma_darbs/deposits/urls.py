from django.urls import path
from . import views


urlpatterns = [
    path('', views.DepositListView.as_view(), name='index'),
    path('deposits/new/', views.AddDepositFormView.as_view(), name='add-deposit'),
    path('deposit/<pk>/', views.ShowDepositView.as_view(), name='show-deposit'),
]