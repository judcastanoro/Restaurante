from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rlbApp.serializers.reservaSerializer import ReservaSerializer   

class ReservaCreateView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = ReservaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        reservaData = {
            'fecha_reserva':request.data['fecha_reserva'],
            'cant_personas':request.data['cant_personas'],
            'observaciones':request.data['observaciones'],
            'id_cliente_fk':request.data['id_cliente_fk'] #enviarlo por medio del frontend 
        }

        return Response(status=status.HTTP_201_CREATED)