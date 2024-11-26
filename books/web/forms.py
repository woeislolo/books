from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm

from .models import *


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'about', 'added_by']


class LoginUserForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ['username', 'password']


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Reader
        fields = UserCreationForm.Meta.fields + ('email',)


class ResetPasswordForm(PasswordResetForm):
    pass