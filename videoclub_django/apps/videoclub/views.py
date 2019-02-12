from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.template.loader import render_to_string
from django.contrib import messages
from django.views.generic import TemplateView, DetailView, ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from apps.videoclub.forms import *
from apps.videoclub.models import Pelicula, Director, Actor

# Mis decoradores

staff = [
    login_required,
    staff_member_required(login_url='forbidden')
]

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

class Forbidden(TemplateView):
    template_name = "videoclub/forbidden.html"

class PeliculasManage(ListView):
    model = Pelicula
    template_name = "videoclub/peliculas_manage.html"

    @method_decorator(staff)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class PeliculasEdit(SuccessMessageMixin, UpdateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = "videoclub/peliculas_edit.html"
    success_url = reverse_lazy('peliculas_manage')  

    def form_valid(self, form):
        if form.is_valid:
            messages.success(
                self.request,
                "Película editada correctamente: {}".format(
                    form.cleaned_data['titulo']),
                extra_tags='edit'
                )
            return super(PeliculasEdit, self).form_valid(form)
        else:
            messages.error(self.request, "Algo ha salido mal")

class PeliculasDelete(DeleteView):
    model = Pelicula
    template_name = "videoclub/peliculas_delete.html"
    success_url = reverse_lazy('peliculas_manage')
    success_message = "La siguiente película se ha eliminado correctamente"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message, extra_tags='success, delete')
        return super(PeliculasDelete, self).delete(request, *args, **kwargs)

class PeliculasCreate(SuccessMessageMixin, CreateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = "videoclub/peliculas_create.html"
    success_url = reverse_lazy('peliculas_manage')

    def form_valid(self, form):
        if form.is_valid:
            messages.success(
                self.request,
                "{} se ha añadido a la base de datos".format(
                        form.cleaned_data['titulo']
                    ),
                extra_tags='add success'
            )
            return super(PeliculasCreate, self).form_valid(form)
        else:
            messages.error(self.request, "Algo ha salido mal")
