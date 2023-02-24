from django.db import models


class Productos(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    codigo = models.IntegerField(unique=True)
    memoria = models.CharField(max_length=50)
    camara = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    bateria = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="avatares")
