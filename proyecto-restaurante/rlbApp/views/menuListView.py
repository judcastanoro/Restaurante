from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response


from rlbApp.models.plato import Plato
from rlbApp.serializers.platoSerializer import PlatoSerializer

class MenuListView(generics.ListAPIView):
    queryset = Plato.objects.all().order_by('categoria')
    serializer_class = PlatoSerializer
    

