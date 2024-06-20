from django import forms
from .custom_field import MultipleFileField

class FileUploadForm(forms.Form):
    file = MultipleFileField(required=True)

class ImageUploadForm(forms.Form):
    file = forms.ImageField(required=True)
