from .models import Usuarios, Textos, Comentarios
from .forms import UsuariosForm, TextosForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

def Index(request):
    contexto = {}
    return render(request, template_name='Common/Inicio.html', context=contexto)

def listaUsuarios(request):
    contexto = {
        "usuarios": Usuarios.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='Common/usuarios.html',
        context=contexto,
    )
    return http_response

def listaTextos(request):
    contexto = {
        "textos": Textos.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='Common/textos.html',
        context=contexto,
    )
    return http_response

def crearUsuario(request):
    formulario = UsuariosForm()
    if request.method == "POST":
        formulario = UsuariosForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            url_exitosa = reverse('listaUsuarios')
            return redirect(url_exitosa)
    contexto = {'formulario': formulario}
    return render(request, 'Common/crearUsuario.html', context=contexto)

def crearTexto(request):
    formulario = TextosForm()
    if request.method == "POST":
        formulario = TextosForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            url_exitosa = reverse('listaTextos')
            return redirect(url_exitosa)
    contexto = {'formulario': formulario}
    return render(request, 'Common/crearTexto.html', context=contexto)

def buscarUsuario(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        usuario = Usuarios.objects.filter(nombre__icontains=busqueda)
        contexto = {
            "usuarios": usuario
        }
        http_response = render(
            request=request,
            template_name='Common/usuarios.html',
            context=contexto,
        )
        return http_response
    
def buscarTexto(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        textos = Textos.objects.filter(titulo__icontains=busqueda)
        contexto = {
            "textos": textos
        }
        http_response = render(
            request=request,
            template_name='Common/textos.html',
            context=contexto,
        )
        return http_response
