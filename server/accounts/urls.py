from django.urls import path, include

from rest_framework import routers
from . import views

urlpatterns = [
    path('api/login/', views.UserLogin.as_view(), name='login'),
    path('api/register/', views.UserRegister.as_view(), name='register'),
    path('api/logout/', views.UserLogout.as_view(), name='logout'),
    path('api/user/<str:username>/', views.UserView.as_view(), name='user_view'),
    path('api/profile/', views.ProfileView.as_view(), name='profile'),
]
