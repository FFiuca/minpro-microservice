from rest_framework.test import APITestCase, APITransactionTestCase
from faker import Faker
from django.urls import reverse
from django.core.management import call_command
from man_user.factory.factory import AdminFactory, Kong_JWTFactory
from master.models import Status
from django.db import connection

class LoginTest(APITestCase):
    fixtures = ['master']

    def setUp(self) -> None:
        # super().setUp()


        # call_command('seed')
        # status = Status.objects.create(status_name='zz')
        self.user = AdminFactory().user
        print('zz', self.user)
        Kong_JWTFactory.create(user=self.user)
        print('zz2')

    def test_login(self):
        response = self.client.post(reverse('man_user:auth.login'), data={
            'email': self.user.email,
            'password': self.user.username,
        })
        print(response.json())

        self.assertTrue(response.status_code==200)
