import json

from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from search_indexes.documents.polygon import PolygonDocument


class PolygonDocumentSerializer(DocumentSerializer):
    geo = serializers.SerializerMethodField()

    class Meta:
        document = PolygonDocument
        fields = ('name', 'price', 'provider_name')

    def get_geo(self, obj):
        return {'type': 'Point', 'coordinates': [obj.geo.lat, obj.geo.lon]}
