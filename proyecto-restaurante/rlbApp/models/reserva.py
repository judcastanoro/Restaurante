#modelo para almacenar la informacion de reservas

from django.db import models
from .cliente import Cliente

class Reserva(models.Model):
    id_reserva = models.BigAutoField(primary_key=True)
    id_cliente_fk = models.ForeignKey(Cliente, related_name='reserva', null=True, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField('Fecha reserva', auto_now_add=True, editable=False)
    cant_personas = models.IntegerField('Cantidad personas',default=0)
    observaciones = models.CharField('Observaciones', max_length=500)