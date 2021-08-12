from django.test import TestCase
from providers.tests.factories import ProviderFactory
from polygons.tests.factories import PolygonFactory


class SearchTest(TestCase):

    def setUp(self):
        self.url = '/search/polygon/'
        self.provider = ProviderFactory()
        self.polygon = PolygonFactory(provider=self.provider)

    def test_search_poligon(self):
        url = '{}?geo__geo_distance=100000km__12.04__-63.93'.format(self.url)
        response = self.client.get(url).json()
        assert response['count'] == 1
