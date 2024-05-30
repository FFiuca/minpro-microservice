from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from man_user.function.kong.jwt import JWTAction
from .test_register import RegisterTest
from faker import Faker
from man_user.models import Kong_JWT, Kong_JWT_Token
from man_user.factory.factory import Kong_JWTFactory
from man_user.function.kong.kong import KongBase
from main.url_helper import switch_to_kong_host
from django.urls import reverse
from man_user.test.test_login import LoginTest
import requests
import json
from django.forms import model_to_dict

fake = Faker()

class TestKong(APITestCase):
    fixtures = ['master']

    def setUp(self) -> None:
        super().setUp()

        self.user = Kong_JWTFactory.create().user
        # self.token = JWTAction().generate_token(user=self.user)

        self.client = APIClient()
        # self.client.credentials();
        # self.login = LoginTest().test_login()

    def test_create_jwt(self):
        cls = JWTAction()
        create = cls.create({'user': self.user})
        print(create)
        self.assertNotEqual(create.jwt_id, None)

        return create

    def test_generate_token(self):
        jwt = self.test_create_jwt()
        token = JWTAction().generate_token(user=self.user)

        self.assertTrue(isinstance(token, Kong_JWT_Token))
        return token

    """
    it can't be done because. return always user does't exist due different db at different runtime,
    when you run in testing mode, it will hit the original runserver but your data from testing db.
    use your testing data instead and no calling from kong. when you run in postman is success, it can be guarantine that when you deploy is success too.
    simply, just make sure your function in your microservice running well. integration testing will be test in next deploy
    """
    def test_authorization(self):
        token = self.test_generate_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+ token.token)

        print('test_authorization:1', "\n", token, "\n",model_to_dict(token.kong_jwt), model_to_dict(self.user))

        data = {
            'permission': ['man_user:add_kong_jwt'],
            'group': ['admin'],
        }
        print('auu', 'Bearer '+ token.token, "\n", switch_to_kong_host(reverse('man_user|authorization')))
        response = requests.post(
            switch_to_kong_host(reverse('man_user|authorization')),
            data=data,
            headers={
                'beh': 'Bearer '+ token.token,
                'authorization': 'Bearer '+ token.token,
                'content-type': 'application/json'
            }
        )
        print(dir(response), "\n", response.json(), "\n", json.dumps(data))

        self.assertNotEqual(response.status_code, 200)

    def test_authorization_success(self):
        token = self.test_generate_token()
        self.client.login(username=self.user.username, password=self.user.username)

        print('test_authorization:1', "\n", token, "\n",model_to_dict(token.kong_jwt), model_to_dict(self.user))

        data = {
            'permission': ['man_user:add_kong_jwt'],
            'group': ['admin'],
        }

        response = self.client.post(
            reverse('man_user|authorization'),
            data=json.dumps(data),
            # headers={
            #     'beh': 'Bearer '+ token.token,
            #     'authorization': 'Bearer '+ token.token,
            #     'content-type': 'application/json'
            # }
            content_type='application/json', # required to automatic parse. it to determine what type must be parse by DRF
        )
        print(dir(response), "\n", response.json())

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.json()['data'].get('group'), None)
