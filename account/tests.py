
from django.test import TestCase, Client, RequestFactory

from django.contrib.auth.models import User

class AccountTestCase(TestCase):

    def setUp(self):
        self.request_invalid_user_mock = {'username': 'abc', 'password': 'xyz'}
        self.request_valid_user_mock = {'username': 'abcd', 'password': '1234'}
        self.login_uri = '/account/login'

    def test_loginInValid(self):
        client = Client()
        response = client.post(self.login_uri, self.request_invalid_user_mock)
        self.assertEqual(response.status_code, 200)

    def test_loginValid(self):
        client = Client()
        response = client.post(self.login_uri, self.request_valid_user_mock)
        self.assertEqual(response.status_code, 200)
