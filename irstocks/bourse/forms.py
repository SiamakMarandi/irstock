from django import forms
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField
from django.core.exceptions import ValidationError
# from django.contrib.auth.models import User
from .models import User
from django.contrib.auth import get_user_model


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', )


