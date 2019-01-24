
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.auth.decorators import login_required

from apps.videoclub.views import *

urlpatterns = [
    path(
        '',
        login_required(VideoclubIndex.as_view()),
        name='vista_index'
    ),
    path(
        'pelicula/<int:pk>/',
        login_required(PeliculaDetailView.as_view()),
        name='pelicula'
    ),
    path(
        'director/<int:pk>/',
        login_required(DirectorDetailView.as_view()),
        name='director'
    ),
    path(
        'actor/<int:pk>/',
        login_required(ActorDetailView.as_view()),
        name='actor'
    ),
    path(
        'peliculas/',
        login_required(PeliculasList.as_view()),
        name='peliculas'
    ),
    path(
        'directores/',
        login_required(DirectoresList.as_view()),
        name='directores'
    )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
