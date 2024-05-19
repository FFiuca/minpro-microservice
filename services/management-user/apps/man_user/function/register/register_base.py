# from man_user.models import User
from django.contrib.auth.models import User
from faker import Faker

fake = Faker()

class RegisterBase:
    # type = 'customer'

    def __init__(self, *args, **kwargs) -> None:
        pass

    def register(self, *args, **kwargs):
        is_active= 1

        email = kwargs['email']
        username = kwargs.get('username') or None
        first_name = kwargs.get('first_name') or None
        last_name = kwargs.get('last_name') or None
        password = kwargs.get('password')

        if username is None:
            username = fake.user_name() # give random username

        if password is None:
            raise Exception('password is empty')
        elif email is None:
            raise Exception('email is empty')

        user= User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name, is_active=is_active)
        if user is None:
            raise Exception('create user failed')

        return user

    def test(self):
        pass

