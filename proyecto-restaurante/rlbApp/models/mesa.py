#modelo para almacenar la informacion de mesas

from django.db import models
from .cliente import Cliente

class Mesa(models.Model):
    id_mesa = models.BigAutoField(primary_key=True)
    cliente = models.ManyToManyField(Cliente, related_name='mesa')
    numero_mesa = models.CharField('Numero mesa', max_length=100, unique=True)
    capacidad = models.IntegerField('Capacidad')
    disponible = models.BooleanField('Disponible', default=True)