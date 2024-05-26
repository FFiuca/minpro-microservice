from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from man_user.function.kong.jwt import JWTAction
from .test_register import RegisterTest
from faker import Faker
from man_user.models import Kong_JWT
from man_user.factory.factory import Kong_JWTFactory

fake = Faker()

class TestKong(APITestCase):
    fixtures = ['master']

    def setUp(self) -> None:
        super().setUp()

        self.user = Kong_JWTFactory.create().user

    def test_create_jwt(self):
        cls = JWTAction()
        create = cls.create({'user': self.user})
        print(create)
        self.assertNotEqual(create.jwt_id, None)
