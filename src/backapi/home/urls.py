from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

import home.views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='home/login.html'), name='login' ),
    path('logout/', auth_views.LogoutView.as_view(template_name='home/logout.html'), name='logout'),
    path('', TemplateView.as_view(template_name='home/home.html'), name='home'),
]
