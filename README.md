# Partorum

Um sistema de gerenciamento de notas de leitura desenvolvido para a disciplina de "Tópicos Especiais em Engenharia de Software: Programação Web", CEFET-MG 2018/2.

Integrantes do projeto: Ana (@analuizatrz), Gabriela (@gabiapple) e Matheus (@Airak)

## Instalação (linux e mac)

Para execução do projeto siga os seguintes passos:

1. Instale o [virtualenv](https://pypi.python.org/pypi/virtualenv) e o [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/). Eles possibilitam a criação de vários ambientes virtuais para o gerenciamento de projetos (em python), evitando conflitos e outros tipos de problemas.

```shell
pip install virtualenv
pip install virtualenvwrapper
```

2. Crie e acesse um ambiente virtual definindo como padrão a versão 3 do python.

```shell
mkvirtualenv --python=`which python3` envName
workon envName
```

3. Clone o repositório do projeto no github (isto criará uma pasta com o nome do projeto no diretório atual).

```shell
git clone https://github.com/Airak/partorum.git
```

4. Instale as dependências do projeto.

```shell
cd partorum
pip install -r requirements.txt
```

5. Rode a aplicação.

```shell
cd api
python manage.py runserver
```

6. Abra o seu navegador e acesse:

http://127.0.0.1/8000
