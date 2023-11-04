from django.urls import path, include

from rest_framework import routers
from . import views
from django.contrib.auth import views as djangoViews
urlpatterns = [
    path('api/login/', views.UserLogin.as_view(), name='login'),
    path('api/register/', views.UserRegister.as_view(), name='register'),
    path('api/org_register/', views.OrganizationRegister.as_view(), name='org_register'),
    path('api/logout/', views.UserLogout.as_view(), name='logout'),
    path('api/session/', views.SessionView.as_view(), name='api-session'),
    path('api/csrf/', views.get_csrf.as_view(), name='api-csrf'),
    path('api/user/<str:username>/', views.UserView.as_view(), name='user_view'),
    path('api/profile/', views.ProfileView.as_view(), name='profile'),

    # path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
    # path('api/password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('api/reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('api/reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('api/password-change/', djangoViews.PasswordChangeView.as_view(), name='password_change'),
    path('api/password-change/done/', djangoViews.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('api/test/', views.front_test.as_view(), name='front_test'),
    path('api/legal/<str:filename>/', views.getMD.as_view(), name='dm_view'),
]
