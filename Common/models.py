from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

class Usuarios(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    usuario = models.CharField(max_length=20)
    pais = models.CharField(max_length=20)
    correo = models.EmailField()
    
class Textos(models.Model):
    titulo = models.CharField(max_length=40)
    texto = models.CharField(max_length=480)
    image = models.ImageField(upload_to='images/', blank=True)
    autor = models.ForeignKey(Usuarios, on_delete=models.CASCADE)


class Comentarios(models.Model):
    comentario = models.CharField(max_length=240)
    autor = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    texto = models.ForeignKey(Textos, on_delete=models.CASCADE)