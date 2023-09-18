from django.test import TestCase
from django.urls import reverse


class TestShortener(TestCase):

    def test_create_and_get_url(self):
        url = reverse('create_short_url')
        response = self.client.post(url, data={'url': 'https://www.example.com'})
        self.assertEqual(response.status_code, 200)
        short_url = response.json()['url']

        response = self.client.get(short_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['url'], 'https://www.example.com')

    def test_404(self):
        url = reverse('get_short_url', kwargs={'id': '123'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
