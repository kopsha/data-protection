from django.shortcuts import redirect, render, reverse
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout

from backpack.models import PrivatePerson
from backpack.models import PrivatePersonForm


def index(request):
	context = {}
	return render(request, 'backpack/index.html', context)

def logout_view(request):
    logout(request)
    return redirect(reverse('index'))

@login_required
def user_home(request):
	all_dudes = PrivatePerson.objects.all()
	context = {
		'people': all_dudes
	}
	return render(request, 'backpack/user_home.html', context)

@login_required
def private_details(request, id=None):
	if id:
		person = get_object_or_404(PrivatePerson, pk=id)
	else:
		person = PrivatePerson()

	form = PrivatePersonForm(request.POST or None, instance=person)

	if request.method == 'POST' and form.is_valid():
		form.save()
		return redirect(reverse('user_home'))

	return render(request, 'backpack/details.html', {'form':form, 'is_new':(id is None)})
