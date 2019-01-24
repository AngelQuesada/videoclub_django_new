from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView, ListView
from django.contrib.auth.decorators import login_required

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

class PeliculaDetailView(DetailView):
    model = Pelicula
    template_name = "videoclub/pelicula.html"

class DirectorDetailView(DetailView):
    model = Director
    template_name = "videoclub/director.html"

class ActorDetailView(DetailView):
    model = Actor
    template_name = "videoclub/actor.html"

class PeliculasList(ListView):
    model = Pelicula
    template_name = "videoclub/peliculas.html"

class DirectoresList(ListView):
    model = Director
    template_name = "videoclub/directores.html"

class ActoresList(ListView):
    model = Actor
    template_name = "videoclub/actores.html"