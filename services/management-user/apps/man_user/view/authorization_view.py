from rest_framework import views, viewsets
from rest_framework.permissions import IsAuthenticated
from man_user.function.auth.authorization import Authorization
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from django.forms import ValidationError, model_to_dict
from main.response_helper import response_builder, message_error
from man_user.form.authorization_form import AuthorizationForm

class AuthorizationView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    parser_classes=[ JSONParser]

    def check_authorization(self, request):
        form = None
        result= None
        try:
            print('[check_authorization]', "\n", type(request.data))
            form = AuthorizationForm(data=request.data)
            # print('[check_authorization2]')
            if form.is_valid() is False:
                raise ValidationError('form not valid')

            result = Authorization().check_authorization(
                request.user,
                form.cleaned_data.get('group'),
                form.cleaned_data.get('permission')
            )
        except ValidationError as e:
            return response_builder({'error': form.errors}, 400)
        except Exception as e:
            return response_builder({'error': message_error(e)}, 500)

        return response_builder(result, 200)

    def get_auth_user(self, request):
        user = None
        try:
            user = request.user
        except Exception as e:
            return response_builder({'error': message_error(e)}, 500)

        return response_builder(model_to_dict(user), 200)
