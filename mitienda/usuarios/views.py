from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.

def registroUsuario(request):
    if request.method == 'POST':
        formulario = RegistroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/')
    else:
        formulario = RegistroForm()
    contexto = {'formulario':formulario}
    return render(request, 'usuarios/registro.html', contexto)

def usuarioLogin(request):
    if request.method == 'POST':
        formulario = LoginForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST["username"]
            clave = request.POST["password"]
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request,acceso)
                    return redirect('/')
                else:
                    return render(request, 'usuarios/errorLogin.html')
        else:
            return render(request, 'usuarios/errorLogin.html')
    else:
        formulario = LoginForm()
    contexto = {"formulario":formulario}
    return render(request, 'usuarios/login.html', contexto)

@login_required(login_url = "/login")
def usuarioLogout(request):
    logout(request)
    return redirect('/')

@login_required(login_url = "/login")
def editarUsuario(request):
    if request.method == 'POST':
        formulario = EditarUsuarioForm(request.POST, request=request)
        if form.is_valid():
            request.user.email = form.cleaned_data['email']
            request.user.save()
            messages.success(request, 'El email ha sido cambiado con exito!.')
            return redirect(reverse('index'))
    else:
        formulario = EditarUsuarioForm()
    return render(request, 'usuarios/perfil.html', {'formulario': formulario})


class editarUsuarioView(UpdateView):
    model = User
    fields=['username','email', 'password']
    template_name = '/usuarios/perfil.html'
    success_url = '/'
