from django.shortcuts import render
from django.forms.models import model_to_dict

from backpack.models import PrivatePerson

def index(request):
	all_dudes = PrivatePerson.objects.all()
	context = {
		'has_people' : len(all_dudes)>0,
		'people' : all_dudes
	}
	return render(request, 'backpack/index.html', context)

def details(request, private_person_id):
	dude = PrivatePerson.objects.get(pk=private_person_id)
	context = {
		'person' : model_to_dict(dude)
	}
	return render(request, 'backpack/details.html', context)
