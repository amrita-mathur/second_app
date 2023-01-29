from django.urls import path, include
from appTwo import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.users, name='users'),
    path('users_info/', views.users_info, name='users_info'),
]