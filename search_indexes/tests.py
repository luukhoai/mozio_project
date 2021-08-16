from django.test import TestCase
from unittest.mock import patch
from providers.tests.factories import ProviderFactory
from polygons.tests.factories import PolygonFactory
from search_indexes.documents.polygon import PolygonDocument
from polygons.models import Polygon
from providers.models import Provider


class SearchTest(TestCase):

    def setUp(self):
        self.url = '/search/polygon/'
        provider = ProviderFactory()
        self.polygon = PolygonFactory(provider=provider)

    def test_search(self):
        url = '{}?geo__geo_distance=10000km__12.04__-63.93'.format(self.url)
        response = self.client.get(url).json()
        assert response['count'] == 1

    def test_search_outside_distance(self):
        url = '{}?geo__geo_distance=10km__12.04__-63.93'.format(self.url)
        response = self.client.get(url).json()
        assert response['count'] == 0
