from django.urls import path
from django.contrib.auth.views import LoginView
from .views import register, profile, logout_view

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
]

