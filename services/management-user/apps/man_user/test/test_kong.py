from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from man_user.function.kong.jwt import JWTAction
from .test_register import RegisterTest
from faker import Faker
from man_user.models import Kong_JWT

fake = Faker()

class TestKong(APITestCase):
    def setUp(self) -> None:
        super().setUp()

        self.user = User.objects.create_user(username=fake.user_name(), email='test@gmail.com', password='1234')

        Kong_JWT.objects.create(user=self.user, kong_consumer_id='9a1b7792-33cf-4fc0-901e-86f3ab2e97ea')

    def test_create_jwt(self):
        cls = JWTAction()
        create = cls.create({'user': self.user})
        print(create)
        self.assertNotEqual(create.jwt_id, None)
