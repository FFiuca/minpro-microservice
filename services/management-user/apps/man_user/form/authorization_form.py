from django import forms
from extended import forms as forms2


class AuthorizationForm(forms.Form):
    group = forms2.ArrayField()
    permission = forms2.ArrayField()

