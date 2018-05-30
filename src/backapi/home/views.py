from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
	return HttpResponse( "<h3>You've landed on homepage</h3><p>Replace me with render template.</p>" )
