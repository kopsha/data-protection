from django.urls import path

import backpack.views

urlpatterns = [
	path('private_person/<int:id>/', backpack.views.private_details, name='view_person'),
	path('private_person/<int:id>/update/', backpack.views.private_details, name='update_person'),
	path('private_person/create/', backpack.views.private_details, name='create_person'),
	path('user_home/', backpack.views.user_home, name='user_home'),
	path('', backpack.views.index, name='index'),
]
