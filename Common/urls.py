from django.contrib import admin
from django.urls import path
from Common.views import Usuarios, Textos, Comentarios, Index

urlpatterns = [
    path('', Index, name="Index"),
    path('Usuarios/', Usuarios),
    path('Textos/', Textos),
    path('Comentarios/', Comentarios),
]
