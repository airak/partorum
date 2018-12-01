from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from django.contrib.auth.models import User

# Create your views here.
class Clipping(View):

	def get(self, request, *args, **kwargs):
		pass

	def post(self, request, *args, **kwargs):
		pass
