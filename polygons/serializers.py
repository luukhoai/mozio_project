from rest_framework.serializers import ModelSerializer
from .models import Polygon


class PolygonSerializer(ModelSerializer):

    class Meta:
        model = Polygon
        fields = ('name', 'price', 'geo', 'provider')
