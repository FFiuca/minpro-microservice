from django.contrib.auth.models import User
from rest_framework import authentication, exceptions
from man_user.models import Kong_JWT_Token

class CustomBaseAuth(authentication.BaseAuthentication):
     def authenticate(self, request):
        kong_consumer_id = request.headers.get('X-Consumer-Id')

        if not kong_consumer_id:
            return None

        user = None
        try:
            user = User.objects.filter(kong_jwt__kong_consumer_id=kong_consumer_id).first()
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('User doesn\'t exist.')

        token = request.headers.get('Authorization')
        token = token.replace('Bearer ', '')
        try:
            token = Kong_JWT_Token.objects.filter(token=token).first()
        except Kong_JWT_Token.DoesNotExist:
            raise exceptions.AuthenticationFailed('Token doesn\'t exist')

        return (user, token)
