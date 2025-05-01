from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.
list_categoria = (
    ('ANIME', 'Anime'),
    ('AVENTURA', 'Aventura'),
    ('AÇÃO', 'Ação'),
    ('TERROR', 'Terror'),
    ('ROMANCE', 'Romance'),
    ('COMEDIA', 'Comedia'),
    ('DOCUMENTARIO', 'Documentário'),
    ('SUSPENSE', 'Suspense'),
    ('DRAMA', 'Drama'),
    ('INFATIL', 'Infantil'),
)

class Filme(models.Model):
    name = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='thumb_filme')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(choices=list_categoria, max_length=30)
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Usuario(AbstractUser):
    model = models.ManyToManyField(Filme)

class Pergunta(models.Model):
    pergunta = models.CharField(max_length=200)
    resposta = models.TextField(max_length=1000)

    def __str__(self):
        return self.pergunta

class Episodio(models.Model):
    filme = models.ForeignKey("Filme",related_name='episodios', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()
    
    def __str__(self):
        return self.titulo
    
class Buscadecategorias(models.Model):
    name = models.CharField(max_length=100)
    button = models.ForeignKey("Filme", related_name='buttons', on_delete=models.CASCADE)

    def __str__(self):
        return self.name