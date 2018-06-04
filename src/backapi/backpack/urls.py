from django.urls import path

import backpack.views

urlpatterns = [
	path('<int:private_person_id>/details/', backpack.views.details, name='detail'),
	path('user_home/', backpack.views.user_home, name='user_home'),
	path('save_private_data/', backpack.views.save_private_data, name='save_private_data'),
	path('', backpack.views.index, name='index'),
]
