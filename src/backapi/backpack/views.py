from django.shortcuts import redirect, render, reverse
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout

from rest_framework import viewsets, permissions

from backpack import rsa_lab
from backpack.models import PrivatePerson, PrivatePersonForm, PrivatePersonSerializer


def index(request):
	context = {}
	return render(request, 'backpack/index.html', context)

def logout_view(request):
    logout(request)
    return redirect(reverse('index'))

@login_required
def user_home(request):
	all_dudes = list(PrivatePerson.objects.all())
	for person in all_dudes:
		person.email = rsa_lab.encrypt(rsa_lab.get_public_key_backend(), str.encode(person.email)).decode("utf-8")
	context = {
		'people': all_dudes,
		'private_key':rsa_lab.get_private_key_backend()
	}
	return render(request, 'backpack/user_home.html', context)

@login_required
def private_details(request, id=None):
	if id:
		person = get_object_or_404(PrivatePerson, pk=id)
	else:
		person = PrivatePerson()

	form = PrivatePersonForm(request.POST or None, instance=person)

	if request.method == 'POST': 
		post = request.POST.copy()
		post['email'] = rsa_lab.decrypt(rsa_lab.get_private_key_client(), post['email'])
		request.POST = post
		form = PrivatePersonForm(request.POST or None, instance=person)
		if form.is_valid():
			form.save()
		return redirect(reverse('user_home'))

	form['email'].initial = rsa_lab.encrypt(rsa_lab.get_public_key_backend(), str.encode(form['email'].value())).decode("utf-8")
	return render(request, 'backpack/details.html', {'form':form, 'private_key':rsa_lab.get_private_key_backend(),'public_key':rsa_lab.get_public_key_client(), 'is_new':(id is None)})


class PrivateViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = PrivatePerson.objects.all()
    serializer_class = PrivatePersonSerializer
