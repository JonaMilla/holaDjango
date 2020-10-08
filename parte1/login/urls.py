#importando Path para generar URLS
from django.urls import path    
#importando los views para vincular una funcionalidad con una URLS
from .views import login, registro, recuperarContrasena

urlpatterns = [
    path('', login),
    path('registro/', registro),
    path('recuperar-contrasena/', recuperarContrasena)
]