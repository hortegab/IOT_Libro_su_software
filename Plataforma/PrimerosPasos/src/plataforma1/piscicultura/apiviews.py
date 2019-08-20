from rest_framework import generics # libreria generica con clases rapidas para GET, POST
from .models import Temperatura, PH, O2disuelto, Pozo # importa los modelos
from .serializers import TemperaturaSerializer, PHSerializer, O2disueltoSerializer, PozoSerializer # importa los serializers


class TemperaturaAPIPiscicultura(generics.ListCreateAPIView):
    """Esta API permite establecer comunicacion entre el terminal IoT y la base de datos a traves de HTTP
    CreateAPIView contiene a POST para ser utilizados de manera simple """
    queryset = Temperatura.objects.all() 
    serializer_class = TemperaturaSerializer

class PhAPIPiscicultura(generics.CreateAPIView):
    """Esta API permite establecer comunicacion entre el terminal IoT y la base de datos a traves de HTTP
    CreateAPIView contiene a POST para ser utilizados de manera simple """
    queryset = PH.objects.all()
    serializer_class = PHSerializer

class O2DisueltoAPI(generics.CreateAPIView):
    """Esta API permite establecer comunicacion entre el terminal IoT y la base de datos a traves de HTTP
    CreateAPIView contiene a POST para ser utilizados de manera simple """
    queryset = O2disuelto.objects.all()#consulta todos los elementos del modelo cuando se solicita GET
    serializer_class = O2disueltoSerializer

class PozoAPI(generics.ListCreateAPIView):
    """ListCreateAPIView contiene los metodos GET y POST para usar de maner simple """
    queryset = Pozo.objects.all()
    serializer_class = PozoSerializer