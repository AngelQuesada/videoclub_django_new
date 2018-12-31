from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from apps.videoclub.models import Pelicula, Director, Actor

# Create your views here.

class VideoclubIndex(TemplateView):
    
    template_name = "videoclub/index.html"
    
    def peliculas(self):
        return Pelicula.objects.all().order_by('-id')[:6]

    def directores(self):
        return Director.objects.all().order_by('-id')[:6]
        
    def actores(self):
        return Actor.objects.all().order_by('-id')[:6]
