from rest_framework import viewsets, generics, mixins
from rest_framework.decorators import api_view, action
from ..form.register_form import RegisterFormBase
from django.forms import ValidationError
from main.response_helper import response_builder, message_error
from man_user.function.register.register_admin import RegisterAdmin
from man_user.function.register.register_customer import RegisterCustomer

class RegisterAdminView(generics.CreateAPIView):

    def create(self, request):
        data = request.data
        # print(data)
        user = None
        try:
            form = RegisterFormBase(data=data)
            if form.is_valid() is False:
                raise ValidationError('validation error')

            data = form.cleaned_data
            print('form', request.data, data)
            user = RegisterAdmin().register(data)
            print('last')
        except ValidationError as e:
            return response_builder(data=[form.errors, e.error_list], status=400)
        except Exception as e:
            return response_builder(data={
                'error': message_error(e)
            }, status=500)

        return response_builder(user, 200)


class RegisterCustomerView(generics.CreateAPIView):

    def create(self, request):
        data = request.data
        # print(data)
        user = None
        try:
            form = RegisterFormBase(data=data)
            if form.is_valid() is False:
                raise ValidationError('validation error')

            data = form.cleaned_data
            print('form', request.data, data)
            user = RegisterCustomer().register(data)
            print('last')
        except ValidationError as e:
            return response_builder(data=[form.errors, e.error_list], status=400)
        except Exception as e:
            return response_builder(data={
                'error': message_error(e)
            }, status=500)

        return response_builder(user, 200)




