from django import forms
from django.contrib.auth.forms import PasswordResetForm

from .models import *


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'about', 'added_by']


class LoginUserForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ['username', 'password']


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control;'}))



class ResetPasswordForm(PasswordResetForm):
    ...
