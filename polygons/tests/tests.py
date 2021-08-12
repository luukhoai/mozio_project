from django.test import TestCase
import json
from unittest.mock import patch
from providers.tests.factories import ProviderFactory
from polygons.tests.factories import PolygonFactory


class PolygonTest(TestCase):

    @patch('django_elasticsearch_dsl.documents.bulk', return_value=None)
    def setUp(self, *args):
        self.url = '/polygons/'
        self.provider = ProviderFactory()
        self.polygon = PolygonFactory(provider=self.provider)

    def test_get_polygon(self):
        response = self.client.get(
            self.url, content_type='application/json').json()
        assert response['count'] == 1
        assert response['results'][0]['name'] == self.polygon.name

    @patch('django_elasticsearch_dsl.documents.bulk', return_value=None)
    def test_create_polygon(self, *args):
        data = {
            'name': 'Test',
            'price': 0.5,
            'geo': {'type': 'Point', 'coordinates': [1.2, 2.3]},
            'provider': self.provider.id
        }
        response = self.client.post(
            self.url, json.dumps(data), content_type='application/json').json()
        assert response['name'] == 'Test'
        assert response['geo'] == {"type": "Point", "coordinates": [1.2, 2.3]}

    @patch('django_elasticsearch_dsl.documents.bulk', return_value=None)
    def test_update_provider(self):
        data = {
            'name': 'Test2',
            'price': 0.8,
            'geo': {'type': 'Point', 'coordinates': [1.4, 2.3]},
            'provider': self.provider.id
        }
        response = self.client.put(
            '{}{}/'.format(self.url, self.polygon.slug), json.dumps(data),
            content_type='application/json').json()
        assert response['name'] == 'Test2'

    @patch('django_elasticsearch_dsl.documents.bulk', return_value=None)
    def test_delete_provider(self):
        response = self.client.delete(
            '{}{}/'.format(self.url, self.polygon.slug),
            content_type='application/json')
        assert response.status_code == 204

    def test_geo_incorrect_json_format(self):
        data = {
            'name': 'Test',
            'price': 0.5,
            'geo': '{test1111}',
            'provider': self.provider.id
        }
        response = self.client.post(
            self.url, json.dumps(data), content_type='application/json').json()
        assert response['geo'] == 'Geo is invalid'
