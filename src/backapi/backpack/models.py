from django.db import models
from django.utils import timezone
from django.forms import ModelForm

import datetime

class PrivatePerson(models.Model):
	"""store sensitive information for a single person"""
	full_name = models.CharField(max_length=254)
	phone = models.CharField(max_length=32, default='+40 ...')
	email = models.EmailField(default='')
	facebook_url = models.CharField(max_length=254, default='')
	parent_phone = models.CharField(max_length=32, default='')
	parent_email = models.EmailField(default='')
	parent_facebook_url = models.CharField(max_length=254, default='')

	address = models.CharField(max_length=254, default='')
	joined = models.DateField(auto_now_add=True, auto_now=False)
	last_modified = models.DateField(auto_now=True)

	def is_recent(self):
		return self.joined >= timezone.now() - datetime.timedelta(days=1)


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
