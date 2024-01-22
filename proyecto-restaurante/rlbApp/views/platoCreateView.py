from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rlbApp.serializers.platoSerializer import PlatoSerializer


class PlatoCreateView(views.APIView):
  permission_classes = (IsAuthenticated,)
  
  def post(self,request,*args,**kwargs):
    serializer = PlatoSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    platoData = {
      'nombre':request.data['nombre_plato'],
      'precio':request.data['precio'],
      'descripcion':request.data['descripcion'],
      'categoria':request.data['categoria'],
      'dia_semana':request.data['dia_semana']
    }


    return Response(status=status.HTTP_201_CREATED)