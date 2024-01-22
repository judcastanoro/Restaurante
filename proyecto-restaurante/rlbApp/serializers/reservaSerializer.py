from cgi import print_exception
from rest_framework import serializers
from rlbApp.models.reserva import Reserva
from rlbApp.models.cliente import Cliente


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id_reserva', 'fecha_reserva', 'cant_personas', 'observaciones', 'id_cliente_fk']

        def create(self, validated_data):
            reservaInstance = Reserva.objects.create(**validated_data)
            return reservaInstance

        def to_representation(self, obj):
            cliente = Cliente.objects.get(id=obj.id)
            reserva = Reserva.objects.get(id_cliente_fk=obj.id)
            return {
                'id': reserva.id_reserva,
                'fecha_reserva': reserva.fecha_reserva,
                'cant_personas': reserva.cant_personas,
                'observaciones': reserva.observaciones,
                'id_cliente_fk':{
                    'id_cliente':cliente.id_cliente,
                    'nombres':cliente.nombres,
                    'apellidos':cliente.apellidos
                }
            }