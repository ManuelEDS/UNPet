from django.urls import path
from .views import PersonaList
from . import views

urlpatterns = [
    path('login/', PersonaList.as_view(), name='login'),
    path('register/'),
    path('logout/', views.logout_view, name='logout'),
]

