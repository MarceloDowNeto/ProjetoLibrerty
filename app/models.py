from django.db import models

# Create your models here.
class Livros(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)  
    identificacao = models.IntegerField()
    numPaginas = models.IntegerField()
    ano = models.IntegerField()
    sinopse = models.Textfield(max_Length=10000)
