from django.urls import path
from .views import registro, iniciarSesion, salir, perfil

urlpatterns = [
    path('', iniciarSesion, name='iniciarSesion'),#www.midominio.cl/
    path('registro/', registro, name='registro'),#www.midominio.cl/registro/
    path('salir/', salir, name='salir'),#www.midominio.cl/salir/
    path('perfil/', perfil, name='perfil')#www.midominio.cl/perfil/
    
]