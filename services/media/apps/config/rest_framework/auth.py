from rest_framework import authentication, exceptions
from django.contrib.auth.models import User
import logging
import json
from config.kong import KongBase
import requests
from config.service_provider import ManUserProvider
from main.response_helper import message_error

log = logging.getLogger(__name__)

class CustomBaseAuth(authentication.BaseAuthentication):
    def authenticate(self, request):
        kong_consumer_custom_id = request.headers.get('X-Consumer-Custom-Id')
        # print('masuk ini', kong_consumer_id)
        if not kong_consumer_custom_id:
            return None

        user = None
        try:
            user = self.full_user(kong_consumer_custom_id)

        except Exception as e:
            log.debug('[base auth debug] except: '+ json.dumps(dict(request.headers)))
            raise exceptions.AuthenticationFailed('User doesn\'t exist. ' + message_error(e))

        token = None

        # print(user, token)
        return (user, token)

    # must hit man_user_service directly
    def full_user(self, kong_consumer_custom_id):
        header = {
            'X-Consumer-Custom-Id': kong_consumer_custom_id
        }

        response = requests.post(ManUserProvider().svc.host_main+ '/man_user/user/man_user/get_auth_user/', headers=header)
        if response.status_code!=200:
            return None

        return response.json()['data']


    def simple_user(self, kong_consumer_custom_id):
        return {
            'kong_consumer_custom_id': kong_consumer_custom_id,
            'id': kong_consumer_custom_id,
            'pk': kong_consumer_custom_id,
        }
