from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def login(request):
    return render(
        request,
        'login/ingreso.html'
    )

def registro(request):
    context = {
        "titulo":"Registrando el nuevo usuario"
    }
    return render(
        request,
        'login/registro.html',
        context
    )

def recuperarContrasena(request):
    context = {
        "titulo":"Recuperar contraseña"
    }
    return render(
        request,
        'login/contrasena.html',
        context
    )
