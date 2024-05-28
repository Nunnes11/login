from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.urls import path
from .forms import LoginForm

class LoginPersonalizado(LoginView):
    authentication_form = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('profile')

