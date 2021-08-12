from rest_framework.serializers import ModelSerializer
from .models import Polygon
from decimal import Decimal, InvalidOperation
from django.core.exceptions import ValidationError


class PolygonSerializer(ModelSerializer):

    class Meta:
        model = Polygon
        fields = ('name', 'price', 'geo', 'provider')

    def validate_geo(self, obj):
        if isinstance(obj, dict) and obj.get('type', None) == 'Point':
            if isinstance(obj.get('coordinates', None), list):
                coordinates = obj['coordinates']
                try:
                    Decimal(coordinates[0])
                    Decimal(coordinates[1])
                    return obj
                except InvalidOperation:
                    pass
        raise ValidationError('Geo is invalid')
