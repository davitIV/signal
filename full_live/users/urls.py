from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fetch_users/', views.fetch_users, name='fetch_users'),
]
