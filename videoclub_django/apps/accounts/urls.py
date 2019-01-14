
from django.urls import path
from django.conf import settings
from django.contrib.auth.views import LoginView, PasswordResetView
from django.contrib.auth import logout
from django.contrib.staticfiles.urls import static

from apps.accounts.views import Registro, ResetPassword

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('registrarse/', Registro.as_view(), name='signup'),
    # path('reset_password/', PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='reset_password'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
