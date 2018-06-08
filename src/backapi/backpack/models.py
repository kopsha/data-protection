from django.db import models
from django.utils import timezone
from django.forms import ModelForm
from django_cryptography.fields import encrypt

import datetime

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from base64 import b64decode


class PrivatePerson(models.Model):
	"""store sensitive information for a single person"""
	full_name = encrypt(models.CharField(max_length=254))
	phone = encrypt(models.CharField(max_length=32, default='+40 ...'))
	email = encrypt(models.EmailField(default=''))
	facebook_url = encrypt(models.CharField(max_length=254, default=''))
	parent_phone = encrypt(models.CharField(max_length=32, default=''))
	parent_email = encrypt(models.EmailField(default=''))
	parent_facebook_url = encrypt(models.CharField(max_length=254, default=''))

	address = encrypt(models.CharField(max_length=254, default=''))
	joined = encrypt(models.DateField(auto_now_add=True, auto_now=False))
	last_modified = models.DateField(auto_now=True)

	def is_recent(self):
		return self.joined >= timezone.now().date() - datetime.timedelta(days=1)


class PrivatePersonForm(ModelForm):
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
	def decrypt_email(self,email):
		f = open('privatekey.pem','r')
		key = RSA.importKey(f.read())
		cipher = PKCS1_OAEP.new(key, hashAlgo=SHA256)
		decrypted_message = cipher.decrypt(b64decode(email))
		print(decrypted_message)
		return decrypted_message
