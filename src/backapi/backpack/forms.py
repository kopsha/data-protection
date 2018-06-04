from django.forms import ModelForm
from backpack.models import PrivatePerson

class PPForm(ModelForm):
	class Meta:
		model = PrivatePerson
		fields = [
			'full_name',
			'phone',
			'email',
			'facebook_url',
			'parent_phone',
			'parent_email',
			'parent_facebook_url',
			'address'
		]
