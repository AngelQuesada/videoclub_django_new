
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', include('apps.videoclub.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

