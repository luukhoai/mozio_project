from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_GEO_DISTANCE,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    IdsFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    SearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet
from django_elasticsearch_dsl_drf.pagination import PageNumberPagination

from .documents.polygon import PolygonDocument
from .serializers import PolygonDocumentSerializer


class PolygonDocumentView(BaseDocumentViewSet):
    """
        Search Polygon by filter geo data. \
        Example: /search/polygon/?geo__geo_distance=100000km__12.04__-63.93
    """

    document = PolygonDocument
    serializer_class = PolygonDocumentSerializer
    pagination_class = PageNumberPagination
    filter_backends = [
        FilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]
    # Define search fields
    search_fields = (
        'price',
    )
    # Define filter fields
    filter_fields = {
        'price': 'price'
    }
    # Define ordering fields
    ordering_fields = {
        'price': 'price'
    }
    ordering = ('price',)
    geo_spatial_filter_fields = {
        'geo': {
            'lookups': [
                LOOKUP_FILTER_GEO_DISTANCE,
            ],
        },
    }
