from django.db import models

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