from django.shortcuts import render
from rest_framework import viewsets, mixins, views
from rest_framework.permissions import IsAuthenticated
from django.forms import ValidationError
from .forms.forms import FileUploadForm
from main.response_helper import response_builder, message_error
from .functions.upload import Upload
from django.forms import model_to_dict
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

class UploadView(viewsets.ViewSet):
    # permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def upload(self, request):
        form= None
        result= None

        # try:
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid() is False:
            raise ValidationError('validation error')

        result = Upload().upload(request.FILES.getlist('file'))
        # except ValidationError as e:
        #     return response_builder({'error': form.errors}, 400)
        # except Exception as e:
        #     return response_builder({'error': message_error(e)}, 500)

        return response_builder([model_to_dict(f) for f in result], 200)
