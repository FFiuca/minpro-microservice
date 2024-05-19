from django import forms
# from man_user.models import User

class RegisterFormBase(forms.Form):
    full_name = forms.CharField(required=True, max_length=50)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    password_confirm = forms.CharField(required=True)
    mobile_phone = forms.IntegerField(required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # check = User.objects.filter(email=email).count()

        # if check>0:
        #     raise forms.ValidationError('email has taken')

        return email

    def clean_password_confirm(self):
        password_confirm = self.cleaned_data.get('password_confirm')
        if self.cleaned_data.get('password')!=password_confirm:
            raise forms.ValidationError('password not match')

        return password_confirm
