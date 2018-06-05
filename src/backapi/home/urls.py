from django.urls import path, include
from django.views.generic.base import TemplateView

import home.views

urlpatterns = [
    path('old/', TemplateView.as_view(template_name='home/home.html'), name='home'),
]
