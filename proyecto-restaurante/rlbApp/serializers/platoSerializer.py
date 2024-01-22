from cgi import print_exception
from rest_framework import serializers
from rlbApp.models.plato import Plato

class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plato
        fields = [
            'nombre_plato',
            'precio',
            'descripcion',
            'categoria',
            'dia_semana'
        ]       
