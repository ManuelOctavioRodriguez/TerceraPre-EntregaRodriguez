from django.contrib import admin
from django.urls import path
from .views import Index, listaTextos, listaUsuarios, crearUsuario, crearTexto

urlpatterns = [
    path('', Index, name="Index"),
    path('usuarios2/', listaUsuarios, name="usuarios"), 
    path('textos/', listaTextos, name="textos"),
    path('crearUsuario/', crearUsuario, name="crearUsuario"),
    path('crearTexto/', crearTexto, name="crearTexto"),
]
