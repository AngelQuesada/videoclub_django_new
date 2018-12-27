from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from apps.videoclub.models import Pelicula

# Create your views here.

class VideclubIndex(ListView):
    model = Pelicula
    queryset = Pelicula.objects.all().order_by('-id')[:6]
    template_name = "videoclub/index.html"
