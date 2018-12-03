from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.contrib.auth.models import User
from . import models

class ClippingSave():
	model = models.Recorte
	fields = ['texto', 'autor', 'livro', 'posicao']
	template_name = 'create_clipping.html'
	success_url = reverse_lazy('core:home')


class ClippingCreate(LoginRequiredMixin, ClippingSave, CreateView):

	def form_valid(self, form):
		clipping = form.save(commit=False)
		clipping.user = self.request.user
		clipping.save()
		return super(ClippingSave, self).form_valid(form)

class ClippingUpdate(LoginRequiredMixin, ClippingSave, UpdateView):
	pass

class ClippingDelete(LoginRequiredMixin, DeleteView):
    model = models.Recorte
    success_url = reverse_lazy('core:home')
    template_name = 'clipping_confirm_delete.html'

@method_decorator(cache_page(60 * 5), name='dispatch')
class ClippingListView(LoginRequiredMixin, ListView):

	template_name = 'list_clipping.html'
	model = models.Recorte
	cache_timeout = 60

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['user'] = self.request.user
		return context

	def get_queryset(self):
		queryset = models.Recorte.objects.filter(user=self.request.user)
		return queryset