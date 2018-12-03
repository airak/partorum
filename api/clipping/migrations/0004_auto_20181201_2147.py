# Generated by Django 2.1.3 on 2018-12-01 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clipping', '0003_auto_20181201_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='titulo',
            field=models.CharField(max_length=200, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='recorte',
            name='posicao',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Posição/Página'),
        ),
    ]