from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100, verbose_name="Nombre de la clasificación")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")
    class Meta:
        verbose_name="categoria"
        verbose_name_plural="categorias"
        ordering=['-name']

    def __str__(self):
        return self.name



class Clasificaciones(models.Model):
    title=models.CharField(max_length=100, verbose_name="Título")
    content=models.TextField(verbose_name="Descipción")
    author=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    clasification=models.ManyToManyField(Category, verbose_name="Clasificación")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")

    class Meta:
        verbose_name="entrada"
        verbose_name_plural="entradas"
        ordering=['-created']

    def __str__(self):
        return self.title