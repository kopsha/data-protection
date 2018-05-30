from django.db import models
from django.utils import timezone

import datetime

class PrivatePerson(models.Model):
	"""store sensitive information for a single person"""
	full_name = models.CharField(max_length=254)
	email = models.EmailField()
	address = models.CharField(max_length=254)
	phone = models.CharField(max_length=32)
	joined = models.DateField(auto_now_add=True, auto_now=False)
	last_modified = models.DateField(auto_now=True)

	def is_recent(self):
		return self.joined >= timezone.now() - datetime.timedelta(days=1)
