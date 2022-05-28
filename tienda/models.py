from pyexpat import model
from django.db import models

class Producto(models.Model):
    descripcion = models.CharField("descripcion", max_length=300)
    cantidad = models.IntegerField("cantidad")
    precio = models.FloatField("precio")
