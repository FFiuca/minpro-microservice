from rest_framework import mixins, generics, viewsets, views
from rest_framework import authentication, permissions
from man_user.form.login_form import LoginForm
from django.forms import ValidationError
from main.response_helper import response_builder
from man_user.function.auth.auth import Login

class LoginView(views.APIView):
    # permission_classes=[lambda: permissions().IsAuthenticated() is False]

    def post(self, request, *args, **kwargs):
        data = request.data

        form = None
        try:
            form = LoginForm(data=data)

            if form.is_valid() is False:
                raise ValidationError('validation error')

            data = Login().login(form.cleaned_data)

        except ValidationError as e:
            return response_builder({'error': form.errors}, 400)

        return response_builder(data['data'], 200 if data['status'] is True else 400)
class LogoutView(views.APIView):
    def get(self, request):
        pass
