from rest_framework.test import APITestCase, APITransactionTestCase
from faker import Faker
from django.urls import reverse
from django.core.management import call_command
from main.common_helper import extract_digits

fake = Faker(['id_ID'])

class RegisterTest(APITestCase):

    def setUp(self) -> None:

        call_command('seed')
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

