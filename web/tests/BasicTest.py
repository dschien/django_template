__author__ = 'schien'
from django.test import TestCase, Client


class BasicTest(TestCase):
    fixtures = ['/web/fixtures/test_data.json']

    def test_simple_response(self):
        c = Client()
        response = c.get('/web/')
        print response.content
        self.assertTrue(response.content.startswith('Hello World'))

