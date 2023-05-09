from django.contrib import admin
from django.urls import path
from Common.views import Index, listaTextos, listaUsuarios

urlpatterns = [
    path('', Index, name="Index"),
    path('usuarios/', listaUsuarios),
    path('textos/', listaTextos),
]
