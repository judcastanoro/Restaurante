from os import system
from rest_framework import status, views,viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from rlbApp.serializers.platoSerializer import PlatoSerializer
from rlbApp.models import Plato, plato

class PlatoDetailView(generics.ListCreateAPIView):

  serializer_class = PlatoSerializer
  lookup_field = 'dia_semana'
  permission_classes = (IsAuthenticated,)
  #queryset = Plato.objects.all().filter(dia_semana=lookup_field)

  def get_queryset(self):

    return Plato.objects.all().filter(dia_semana = self.request.data['dia_semana']).order_by('categoria')
    