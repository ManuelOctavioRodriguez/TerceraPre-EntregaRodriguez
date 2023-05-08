from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return HttpResponse('Vista Home')

def Usuarios(request):
    return HttpResponse('Vista Usuarios')

def Textos(request):
    return HttpResponse('Vista Textos')

def Comentarios(request):
    return HttpResponse('Vistas Comentarios')