from django.contrib import admin
from django.urls import path
from Common.views import Index, listaTextos, listaUsuarios, crearUsuario, crearTexto

urlpatterns = [
    path('', Index, name="Index"),
    path('Usuarios/', listaUsuarios),
    path('textos/', listaTextos),
    path('crearUsuario/', crearUsuario),
    path('crearTexto/', crearTexto),
]
