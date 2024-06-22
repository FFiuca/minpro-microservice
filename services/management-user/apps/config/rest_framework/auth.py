from django.contrib.auth.models import User
from rest_framework import authentication, exceptions
from man_user.models import Kong_JWT_Token, Kong_JWT, User_Proxy
import logging
import json

log = logging.getLogger(__name__)

class CustomBaseAuth(authentication.BaseAuthentication):
     def authenticate(self, request):
        kong_consumer_custom_id = request.headers.get('X-Consumer-Custom-Id')
        print('masuk ini', kong_consumer_custom_id, request.headers)
        if not kong_consumer_custom_id:
            return None

        user = None
        try:
            print("[authenticate2]", "\n", kong_consumer_custom_id ,Kong_JWT.objects.all(),"\n", Kong_JWT_Token.objects.all(), "\n",User_Proxy.objects.filter(uuid=kong_consumer_custom_id).first())

            user = User.objects.get(user_proxy__pk=kong_consumer_custom_id)
        except User.DoesNotExist:
            log.debug('[base auth debug] except: '+ json.dumps(dict(request.headers)))
            raise exceptions.AuthenticationFailed('User doesn\'t exist.')

        token = request.headers.get('Authorization')
        token = token.replace('Bearer ', '')
        try:
            token = Kong_JWT_Token.objects.get(token=token)
        except Kong_JWT_Token.DoesNotExist:
            raise exceptions.AuthenticationFailed('Token doesn\'t exist')

        # print(user, token)
        return (user, token)
