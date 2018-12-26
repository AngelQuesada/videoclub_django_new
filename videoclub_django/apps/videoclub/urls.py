
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.contrib.staticfiles.urls import static

from apps.videoclub.views import *

urlpatterns = [
    path('', index, name='index'),
]

