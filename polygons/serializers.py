from rest_framework.serializers import ModelSerializer
from .models import Polygon
from decimal import Decimal, InvalidOperation
from django.core.exceptions import ValidationError
from rest_framework.validators import UniqueTogetherValidator


class PolygonSerializer(ModelSerializer):

    class Meta:
        model = Polygon
        fields = ('name', 'price', 'geo', 'provider')
        validators = [
            UniqueTogetherValidator(
                    queryset=Polygon.objects.all(),
                    fields=['name', 'provider']
                )
        ]

    def validate_geo(self, obj):
        """
        Validate geo raw_data
        It should be: {'type': 'Point', 'coordinates': [1.4, 2.3]}
        """
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
