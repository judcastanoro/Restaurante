#modelo para almacenar la informacion de clientes

from django.db import models
from .user import User

class Cliente(models.Model):
    id_cliente = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, related_name='cliente', null=True, on_delete=models.CASCADE)
    nombres = models.CharField('Nombres', max_length=255, null=True)
    apellidos = models.CharField('Apellidos', max_length=255, null=True)
    tipo_documento = models.CharField('Tipo documento', max_length=255)
    numero_documento = models.IntegerField('Numero documento')
    telefono = models.IntegerField('Telefono')