from django.test import TestCase
from clipping.models import Autor, Livro, Recorte
from django.urls import reverse
from django.contrib.auth.models import User

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


class ClippingListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("tester", "te.", "123")
        self.autor = Autor.objects.create(nome="Nicholas Sparks")
        self.livro = Livro.objects.create(
            titulo="A Última Música",
            autor=self.autor
        )

    def test_sem_clippings(self):
        login = self.client.login(username="tester", password="123")
        response = self.client.get(reverse("clipping:list_clipping"))
        self.assertEqual(response.status_code, 200)

    def test_clippings(self):
        login = self.client.login(username="tester", password="123")
        queryset = Recorte.objects.filter(user=self.user)
        Recorte.objects.create(
            texto="Lorem ipsum",
            autor=self.autor,
            livro=self.livro,
            user=self.user
        )
        response = self.client.get(reverse("clipping:list_clipping"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['recorte_list'],
            ['<Recorte: Recorte object (1)>']
        )