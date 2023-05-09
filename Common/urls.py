from django.contrib import admin
from django.urls import path
from Common.views import Usuarios, Textos, Comentarios, Index

urlpatterns = [
    path('', Index, name="Index"),
    path('usuarios/', Usuarios),
    path('textos/', Textos),
    path('comentarios/', Comentarios),
]
