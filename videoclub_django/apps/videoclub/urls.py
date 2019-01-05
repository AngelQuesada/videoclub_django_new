
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static

from apps.videoclub.views import *

urlpatterns = [
    path(
        '',
        VideoclubIndex.as_view(),
        name='vista_index'
    ),
    path(
        'pelicula/<int:pk>/',
        PeliculaDetailView.as_view(),
        name='pelicula'
    )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
