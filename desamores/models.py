from django.db import models

# Create your models here.
class Desamores(models.Model):
    title=models.CharField(max_length=100, verbose_name="Título")
    subtitle=models.CharField(max_length=100, verbose_name="SubTítulo")
    content=models.TextField(verbose_name="Descipción")
    image=models.ImageField(upload_to="desamor", verbose_name="Imagen")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")

    class Meta:
        verbose_name="Poema de Desamor"
        verbose_name_plural="Poemas de Desamor"
        ordering=['-created']

    def __str__(self):
        return self.title