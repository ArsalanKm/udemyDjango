from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label="", required=True)
    first_name = forms.CharField(label="", required=True)
    last_name = forms.CharField(label="", required=True)
    username = forms.CharField(label="", required=True)
    password1 = forms.CharField(label="", required=True, widget=forms.PasswordInput())
    password2 = forms.CharField(label="", required=True, widget=forms.PasswordInput())

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("this email is already registered")
        return self.cleaned_data['email']

    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError("this username is already registered")
        return self.cleaned_data['username']

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

        # if you want to do it to all of them
        for field in self.fields.values():
            field.error_messages = {'required': ''.format(
                fieldname=field.label)}
