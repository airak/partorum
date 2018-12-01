from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.contrib.auth.models import User
from . import models


class ClippingCreate(LoginRequiredMixin, CreateView):

	model = models.Recorte
	fields = ['texto', 'autor', 'livro', 'posicao']
	template_name = 'create_clipping.html'
	success_url = 'core:home'

	def form_valid(self, form):
		clipping = form.save(commit=False)
		clipping.user = self.request.user
		clipping.save()
		return redirect('core:home')

class ClippingUpdate(LoginRequiredMixin, UpdateView):

	model = models.Recorte
	fields = ['texto', 'autor', 'livro', 'posicao']
	template_name = 'clipping_update_form.html'

class ClippingDelete(LoginRequiredMixin, DeleteView):
    model = models.Recorte
    success_url = reverse_lazy('core:home')
    template_name = 'clipping_confirm_delete.html'

class ClippingListView(LoginRequiredMixin, ListView):

	template_name = 'list_clipping.html'
	model = models.Recorte

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

	def get_queryset(self):
		queryset = models.Recorte.objects.filter(user=self.request.user)
		return queryset