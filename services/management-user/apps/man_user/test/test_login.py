from rest_framework.test import APITestCase, APITransactionTestCase
from faker import Faker
from django.urls import reverse
from django.core.management import call_command
from man_user.factory.factory import AdminFactory, Kong_JWTFactory

class LoginTest(APITestCase):
    def setUp(self) -> None:
        super().setUp()

        call_command('seed')

        self.user = AdminFactory.create().user
        Kong_JWTFactory.create(user=self.user)

    def test_login(self):
        response = self.client.post(reverse('man_user:auth.login'), data={
            'email': self.user.email,
            'password': self.user.username,
        })
        print(response.json())

        self.assertTrue(response.status_code==200)
