from django.urls import path

import backpack.views

urlpatterns = [
	path('<int:private_person_id>/details/', backpack.views.details, name='detail'),
	path('user_home/', backpack.views.user_home, name='user_home'),
	path('', backpack.views.index, name='index'),
]
