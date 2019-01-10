from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.views import generic
from django import forms
from apps.accounts.forms import RegistroForm

# Create your views here.


class Registro(CreateView):
    model = User
    template_name = "accounts/registro.html"
    form_class = RegistroForm
    success_url = reverse_lazy('login')
