from .models import Usuarios, Textos, Comentarios
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

def Index(request):
    return render(request, 'Common/Inicio.html')

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