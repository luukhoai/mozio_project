from django.test import TestCase
from unittest.mock import patch
from providers.tests.factories import ProviderFactory
from polygons.tests.factories import PolygonFactory
from search_indexes.documents.polygon import PolygonDocument
from polygons.models import Polygon


class SearchTest(TestCase):

    def setUp(self):
        self.url = '/search/polygon/'
        # self.polygon = Polygon(
        #     name='Test', price=123, provider=self.provider,
        #     geo={'type': 'Point', 'coordinates': [1.2, 2.3]})
        self.polygon = PolygonFactory.build()
        polygonDoc = PolygonDocument()
        with patch('django_elasticsearch_dsl.documents.bulk') as mock:
            polygonDoc.update(self.polygon)
