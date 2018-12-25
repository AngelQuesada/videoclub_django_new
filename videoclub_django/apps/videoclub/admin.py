from django.contrib import admin
from apps.videoclub.models import Actor, Director, Genero, Pelicula, Copia

admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Genero)
admin.site.register(Pelicula)
admin.site.register(Copia)
