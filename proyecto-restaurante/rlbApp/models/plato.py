#modelo para almacenar la informacion de platos

from django.db import models

class Plato(models.Model):
    id_plato = models.BigAutoField(primary_key=True)
    nombre_plato = models.CharField('Nombre plato', max_length=255)
    precio = models.FloatField('Precio', default=0)
    descripcion = models.CharField('Descripcion', max_length=255, null=True)
    categoria = models.CharField('Categoria', max_length=255)
    dia_semana = models.CharField('Dia semana', max_length=10)