from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email"]

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets ={"password":forms.PasswordInput(),}

class EditarUsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email"]
