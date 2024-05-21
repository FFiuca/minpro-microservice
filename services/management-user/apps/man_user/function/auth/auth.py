
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from man_user.function.kong.jwt import JWTAction
from django.forms.models import model_to_dict

class AuthBase:
    def login(self):
        pass

    def logout(self):
        pass

    def not_login(self):
        return Response(data={
            'status': 403,
            'data': {
                'error' : 'You are not logged in.'
            }
        }, status=403)

class Login(AuthBase):
    def login(self, data, *args, **kwargs):
        user = User.objects.filter(email=data['email']).first()

        if user is None:
            return {
                'status': False,
                'data': {
                    'error': 'User not found'
                }
            }

        if check_password(data['password'], user.password) is False:
            return {
                'status': False,
                'data': {
                    'error': 'Password is wrong'
                }
            }

        clss = JWTAction()
        jwt = clss.create({
            'username': user.username,
            'user': user
        })

        return {
            'status': True,
            'data': model_to_dict(jwt)
        }
