from django.urls import path, include
from django.contrib.auth import views as auth_views

from rest_framework import routers

import backpack.views


api_router = routers.DefaultRouter()
api_router.register(r'', backpack.views.PrivateViewSet)

urlpatterns = [
    path('private_person/<int:id>/', backpack.views.private_details, name='view_person'),
    path('private_person/<int:id>/update/', backpack.views.private_details, name='update_person'),
    path('private_person/create/', backpack.views.private_details, name='create_person'),

    path('user_home/', backpack.views.user_home, name='user_home'),

    path('logout/', backpack.views.logout_view, name='logout'),

    path('api/', include(api_router.urls)),

    path('', auth_views.LoginView.as_view(template_name='backpack/index.html'), name='index' ),
]
