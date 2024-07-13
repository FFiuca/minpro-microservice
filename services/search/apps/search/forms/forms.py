from django import forms

class SearchGetForm(forms.Form):
    collection = forms.CharField(required=True)
    data = forms.JSONField(required=False)
    soft_delete = forms.BooleanField(required=False)

class SearchAddParam(forms.Form):
    collection = forms.CharField(required=True)
    data = forms.JSONField(required=True)

class SearchUpdateParam(forms.Form):
    id = forms.CharField(required=True)
    collection = forms.CharField(required=True)
    data = forms.JSONField(required=True)

class SearchDeleteParam(forms.Form):
    id = forms.CharField(required=True)
    collection = forms.CharField(required=True)

class SearchSoftDeleteParam(forms.Form):
    id = forms.CharField(required=True)
    collection = forms.CharField(required=True)

class SearchRetrieveParam(forms.Form):
    id = forms.CharField(required=True)
    collection = forms.CharField(required=True)
