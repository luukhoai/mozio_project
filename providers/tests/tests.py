from django.test import TestCase
import json
from providers.tests.factories import ProviderFactory


class ProviderTest(TestCase):

    def setUp(self):
        self.url = '/providers/'
        self.provider = ProviderFactory()

    def test_get_provider(self):
        response = self.client.get(
            self.url, content_type='application/json').json()
        assert len(response) == 1
        assert response[0]['name'] == self.provider.name

    def test_create_provivder(self):
        data = {
            'name': 'Test',
            'email': 'test@gmail.com',
            'phone_number': '+123456789',
            'language': 'VN',
            'currency': 'USD'
        }
        response = self.client.post(
            self.url, json.dumps(data), content_type='application/json').json()
        assert response['name'] == 'Test'
        assert response['email'] == 'test@gmail.com'

    def test_update_provider(self):
        data = {
            'name': 'Test2',
            'email': 'test@gmail.com',
            'phone_number': '+123456789',
            'language': 'VN',
            'currency': 'USD'
        }
        response = self.client.put(
            '{}{}/'.format(self.url, self.provider.slug), json.dumps(data),
            content_type='application/json').json()
        assert response['name'] == 'Test2'
        assert response['email'] == 'test@gmail.com'

    def test_delete_provider(self):
        response = self.client.delete(
            '{}{}/'.format(self.url, self.provider.slug),
            content_type='application/json')
        assert response.status_code == 204

    def test_validate_phone_number(self):
        data = {
            'name': 'Test',
            'email': 'test@gmail.com',
            'phone_number': '123456789',
            'language': 'VN',
            'currency': 'USD'
        }
        response = self.client.post(
            self.url, json.dumps(data), content_type='application/json').json()
        assert response['phone_number'][0] == \
            "Phone number must be entered in the format: '+999999999'"
