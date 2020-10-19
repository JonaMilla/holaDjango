from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def registro(request):
    #GET
    formulario = UserCreationForm()  
    if request.method == 'POST':
        # entro a POST 
        formulario = UserCreationForm(data = request.POST)
        if formulario.is_valid():
            usuarioRegistrado = formulario.save()
            if usuarioRegistrado is not None:
                login(request, usuarioRegistrado)
                return redirect('/perfil/')

    context = {
        'formulario' : formulario
    }
    return render(
        request,
        'cuenta/registro.html',
        context
    )
    #POST
def iniciarSesion(request):
    #GET
    formulario = AuthenticationForm()
    if request.method == 'POST':
        formulario = AuthenticationForm(data=request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password']

            usuarioLogeado = authenticate(username = username, password = password)
            if usuarioLogeado is not None:
                login(request, usuarioLogeado)
                return redirect('/perfil/')

    context = {
        'formulario' : formulario
    }
    return render(
        request,
        'cuenta/login.html',
        context
    )
    #POST
def salir(request):
    logout(request)
    return redirect('/')

def perfil(request):
    if request.user.is_authenticated:
        return render(
            request,
            'cuenta/perfil.html'
        )
    return redirect('/')