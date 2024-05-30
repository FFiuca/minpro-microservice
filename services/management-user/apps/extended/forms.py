from django import forms

class ArrayField(forms.Field):
    def __init__(self, required=False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.required = required

    def validate(self, value) -> None:
        if not isinstance(value, list):
            raise forms.ValidationError('Value must be list')

        if self.required and len(value)==0:
            raise forms.ValidationError('List is required')
