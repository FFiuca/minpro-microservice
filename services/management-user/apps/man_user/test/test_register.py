from rest_framework.test import APITestCase, APITransactionTestCase
from faker import Faker
from django.urls import reverse
from django.core.management import call_command
from main.common_helper import extract_digits
from man_user import models
from man_user.factory import factory

fake = Faker(['id_ID'])

class RegisterTest(APITestCase):
    fixtures = ['master']

    def setUp(self) -> None:

        # call_command('seed') # not stable, use fixtures instead
        self.build_data()

    def build_data(self):
        password = fake.password(length=10)

        self.data_admin = {
            'full_name': fake.name(),
            'username': fake.user_name(),
            'email': fake.free_email(),
            'password': password,
            'password_confirm': password,
            'mobile_phone': extract_digits(fake.phone_number())
        }

    def test_register_admin(self):
        response = self.client.post(reverse('man_user:register.admin'), self.data_admin)
        json = response.json()
        print(json, response)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json['status'], 200)

        return json

    def test_factory_admin(self):
        print('cok1')
        create = factory.AdminFactory.create_batch(size=2)
        print('cok2')
        check = models.Admin.objects.count()

        self.assertTrue(check>0)
        self.assertGreater(check, 0)

    def test_factory_kong(self):
        kong = factory.Kong_JWTFactory.create()
        check = models.Kong_JWT.objects.count()

        self.assertTrue(check>0)

