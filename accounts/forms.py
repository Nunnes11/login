from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Matricula', max_length=20)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    