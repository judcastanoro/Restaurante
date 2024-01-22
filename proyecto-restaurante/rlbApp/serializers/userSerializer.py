from cgi import print_exception
from rest_framework import serializers
from rlbApp.models.user import User
from rlbApp.models.cliente import Cliente
from rlbApp.serializers.clienteSerializer import ClienteSerializer

class UserSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()
    class Meta:
        model = User
        fields = ['id','username','password','email','cliente']

    def create(self, validated_data): #deserializacion JSON a objeto python
        clienteData = validated_data.pop('cliente')
        userInstance = User.objects.create(**validated_data)
        Cliente.objects.create(user=userInstance, **clienteData)
        return userInstance
    
    def to_representation(self, obj): #serializacion objeto python a JSON
        user = User.objects.get(id=obj.id)
        cliente = Cliente.objects.get(user=obj.id)
        return {
            'id':user.id,
            'username':user.username,
            'email':user.email,
            'cliente':{
                'id_cliente':cliente.id_cliente,
                'nombres':cliente.nombres,
                'apellidos':cliente.apellidos,
                'tipo_documento':cliente.tipo_documento,
                'numero_documento':cliente.numero_documento,
                'telefono':cliente.telefono
            }
        }