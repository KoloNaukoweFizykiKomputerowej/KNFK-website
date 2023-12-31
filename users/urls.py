from django.urls import path
from .views import (
    present_board_members,
    profile,
    register,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('board_members/', present_board_members, name='board-members'),
]
