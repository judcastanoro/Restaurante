from rlbApp.models.cliente import Cliente
from rest_framework import serializers

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'nombres',
            'apellidos',
            'tipo_documento',
            'numero_documento',
            'telefono'
        ]