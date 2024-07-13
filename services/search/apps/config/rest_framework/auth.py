from rest_framework import authentication, exceptions
from django.contrib.auth.models import User
import logging
import json
from config.kong import KongBase
import requests
from config.service_provider import ManUserProvider
from main.response_helper import message_error
from django.utils.dateparse import parse_datetime

log = logging.getLogger(__name__)

class CustomBaseAuth(authentication.BaseAuthentication):
    def authenticate(self, request):
        kong_consumer_custom_id = request.headers.get('X-Consumer-Custom-Id')
        print('masuk ini', kong_consumer_custom_id)
        if not kong_consumer_custom_id:
            return None

        user = None
        try:
            user = self.full_user(kong_consumer_custom_id)

        except Exception as e:
            log.debug('[base auth debug] except: '+ json.dumps(dict(request.headers)))
            raise exceptions.AuthenticationFailed('User doesn\'t exist. ' + message_error(e))

        token = None

        print(user, token)
        return (user, token)

    # must hit man_user_service directly
    def full_user(self, kong_consumer_custom_id):
        header = {
            'X-Consumer-Custom-Id': kong_consumer_custom_id,
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6IjRuT0hZZmw2TFpBeVlmdGVhSGFsR1VyN2xCTEFibGNKIiwidHlwIjoiSldUIn0.eyJlbWFpbCI6ImNhY280YXphMmFhQGdtYWlsLmNvbSIsImtvbmdfY29uc3VtZXJfaWQiOiI4ZGMwOWM0Yi1kNTZkLTQ0ZmMtYjRiNi1mZDYxOTNiMTYwNTQiLCJleHAiOjE3MTY5ODExNDkuNjkxNjY3fQ.4WnwzF-1mjHsmXWhuRbNWBJn6yStDKaV9gIplrZ2uzI',
        }

        response = requests.post(ManUserProvider().svc['host_main']+ '/man_user/user/man_user/get_auth_user/', headers=header)
        if response.status_code!=200:
            return None

        data = response.json()['data']
        data = self.wrap_to_user_model(data)

        print('full_user', response.json(), data)
        return data


    def simple_user(self, kong_consumer_custom_id):
        return {
            'kong_consumer_custom_id': kong_consumer_custom_id,
            'id': kong_consumer_custom_id,
            'pk': kong_consumer_custom_id,
        }

    """
    wrapping into user model class to get built in compatibility
    """
    def wrap_to_user_model(self, data):
        return User(
            id=data['id'],
            password=data['password'],
            last_login=data['last_login'],
            is_superuser=data['is_superuser'],
            username=data['username'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            is_staff=data['is_staff'],
            is_active=data['is_active'],
            date_joined=parse_datetime(data['date_joined']),
            # groups=data['groups'],
            # user_permissions=data['user_permissions'],
        )
