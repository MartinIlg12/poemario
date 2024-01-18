from django.db import models

# Create your models here.
class Clasificaciones(models.Model):
    title=models.CharField(max_length=100, verbose_name="Título")
    content=models.TextField(verbose_name="Descipción")
    author=models.CharField(max_length=100, verbose_name="Autor")
    clasification=models.CharField(max_length=100, verbose_name="Clasificación")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")

    class Meta:
        verbose_name="Clasificación de Autor y Poema"
        verbose_name_plural="Clasificación de Autores y Poemas"
        ordering=['-created']

    def __str__(self):
        return self.title