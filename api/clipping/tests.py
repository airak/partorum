from django.test import TestCase
# from django.tests import Client
from clipping.models import Autor, Livro

# Create your tests here.
class AutorTestCase(TestCase):
    def setUp(self):
        Autor.objects.create(nome="Nicholas Sparks")
        Autor.objects.create(nome="Jojo Moraes")

    def test_autores_str(self):
        autor1 = Autor.objects.get(nome="Nicholas Sparks")
        autor2 = Autor.objects.get(nome="Jojo Moraes")
        self.assertEqual(str(autor1), "Nicholas Sparks")
        self.assertEqual(str(autor2), "Jojo Moraes")

class LivroTestCase(TestCase):
    def setUp(self):
        autor1 = Autor.objects.create(nome="Nicholas Sparks")
        autor2 = Autor.objects.create(nome="Jojo Moraes")
      
        Livro.objects.create(titulo="A Última Música", autor=autor1)
        Livro.objects.create(titulo="Como eu era antes de você", autor=autor2)

    def test_livros_str(self):
        livro1 = Livro.objects.get(titulo="A Última Música")
        livro2 = Livro.objects.get(titulo="Como eu era antes de você")
        self.assertEqual(str(livro1), "A Última Música")
        self.assertEqual(str(livro2), "Como eu era antes de você")
