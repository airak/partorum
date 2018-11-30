from django.db import models
from django.contrib.auth.models import User

class Autor(models.Model):
	nome = models.TextField('Nome')
	data_criacao = models.DateTimeField(auto_now_add=True)
	data_atualizacao = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name = 'Autor'
		verbose_name_plural = 'Autores'

class Livro(models.Model):
	titulo = models.TextField('Título')
	autor = models.ForeignKey(Autor, on_delete=models.PROTECT, related_name='livro', verbose_name='Autor')
	data_criacao = models.DateTimeField(auto_now_add=True)
	data_atualizacao = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.titulo

	class Meta:
		verbose_name = 'Livro'
		verbose_name_plural = 'Livros'

class Recorte(models.Model):
	texto = models.TextField('Recorte')
	data_criacao = models.DateTimeField(auto_now_add=True)
	data_atualizacao = models.DateTimeField(auto_now=True)
	posicao = models.TextField('Posição/Página', null=True, blank=True)

	user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='recorte', verbose_name='Usuario')
	livro = models.ForeignKey(Livro, on_delete=models.PROTECT, related_name='recorte', verbose_name='Livro')
	autor = models.ForeignKey(Autor, on_delete=models.PROTECT, related_name='recorte', verbose_name='Autor')

	class Meta:
		verbose_name = 'Recorte'
		verbose_name_plural = 'Recortes'