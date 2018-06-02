from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

import home.views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login' ),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]
