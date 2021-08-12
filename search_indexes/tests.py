from django.test import TestCase
import json
from polygons.models import Polygon
from providers.tests.factories import ProviderFactory
from polygons.tests.factories import PolygonFactory
from .documents.polygon import PolygonDocument

class SearchTest(TestCase):

    def setUp(self):
        self.url = '/search/polygon/'
        self.provider = ProviderFactory()
        self.polygon = PolygonFactory(provider=self.provider)

    def test_search_poligon(self):
        query = self.polygon.name.split(' ')[0].lower()
        url = '{}?search={}'.format(self.url, query)
        # url = '{}?geo__geo_distance=100000km__12.04__-63.93'.format(self.url)
        print(url)
        response = self.client.get(
            url, content_type='application/json')
        print(response)
        # assert len(response) == 1
