from django.urls import path

import backpack.views

urlpatterns = [
	path('<int:private_person_id>/details/', backpack.views.details, name='detail'),
	path('', backpack.views.index, name='index'),
]
