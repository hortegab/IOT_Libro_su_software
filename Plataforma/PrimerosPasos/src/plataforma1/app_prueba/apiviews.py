from rest_framework import generics 
from .models import AlbumImagenes
from .serializers import AlbumSerializer

class AlbumAPI(generics.CreateAPIView):
    queryset = AlbumImagenes.objects.all()
    serializer_class = AlbumSerializer