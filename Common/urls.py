from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('usuarios/', views.listaUsuarios, name='listaUsuarios'),
    path('crearUsuario/', views.crearUsuario, name='crearUsuario'),
    path('textos/', views.listaTextos, name='listaTextos'),
    path('crearTexto/', views.crearTexto, name='crearTexto'),
    path('comentarios/', views.listaComentarios, name='listaComentarios'),
    path('crearComentario/', views.crearComentario, name='crearComentario'),
    path('buscarUsuario/', views.buscarUsuario, name='buscarUsuario'),
    path('buscarTexto/', views.buscarTexto, name='buscarTexto'),
    path('buscarComentario/', views.buscarComentario, name='buscarComentario'),
]

