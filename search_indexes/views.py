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
    """The BookDocument view."""

    document = PolygonDocument
    serializer_class = PolygonDocumentSerializer
    # pagination_class = PageNumberPagination
    filter_backends = [
        FilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]
    # Define search fields
    search_fields = (
        'name',
        'lat',
        'lng'
    )
    # Define filter fields
    filter_fields = {
        'name': 'name.raw'
    }
    # Define ordering fields
    ordering_fields = {
        'name': 'name.raw'
    }
    ordering = ('name',)
    geo_spatial_filter_fields = {
        'geo': {
            'lookups': [
                LOOKUP_FILTER_GEO_DISTANCE,
            ],
        },
    }

    def get_queryset(self):
        queryset = super(PolygonDocumentView, self).get_queryset()
        return queryset
