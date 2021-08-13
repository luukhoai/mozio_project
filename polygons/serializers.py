from rest_framework.serializers import ModelSerializer, JSONField
from .models import Polygon
from decimal import Decimal, InvalidOperation
from django.core.exceptions import ValidationError
from rest_framework.validators import UniqueTogetherValidator
from drf_yasg import openapi


class PolygonGeoField(JSONField):
    class Meta:
        swagger_schema_fields = {
            "type": openapi.TYPE_OBJECT,
            "title": "Polygon",
            "properties": {
                "type": openapi.Schema(
                    title="Type",
                    type=openapi.TYPE_STRING,
                ),
                "coordinates": openapi.Schema(
                    title="Coordinates",
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Items(type=openapi.TYPE_NUMBER)
                ),
            },
            "required": ["type", "coordinates"],
         }


class PolygonSerializer(ModelSerializer):
    geo = PolygonGeoField()

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
