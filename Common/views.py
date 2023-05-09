from .models import Usuarios, Textos, Comentarios
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse

def Index(request):
    return render(request, 'Common/index.html')

def Home(request):
    return render(request, 'Common/Home.html')

def Usuarios(request):
    return render(request, 'Common/Usuarios.html')

def Textos(request):
    return render(request, 'Common/Textos.html')

def Comentarios(request):
    return render(request, 'Common/Comentarios.html')