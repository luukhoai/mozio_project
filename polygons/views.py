from .models import Polygon
from .serializers import PolygonSerializer
from rest_framework import generics


class PolygonList(generics.ListCreateAPIView):
    queryset = Polygon.objects.all()
    serializer_class = PolygonSerializer


class PolygonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Polygon.objects.all()
    serializer_class = PolygonSerializer
    lookup_field = 'slug'
