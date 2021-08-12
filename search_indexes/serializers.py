import json

from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer


class PolygonDocumentSerializer(DocumentSerializer):
    geo = serializers.SerializerMethodField()

    class Meta:
        fields = ('name', 'price', 'provider_name')

    def get_geo(self, obj):
        return {'type': 'Point', 'coordinates': [obj.lat, obj.lon]}
