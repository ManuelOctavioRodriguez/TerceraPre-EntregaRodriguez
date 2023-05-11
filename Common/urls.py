from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('usuarios/', views.listaUsuarios, name='listaUsuarios'),
    path('crearUsuario/', views.crearUsuario, name='crearUsuario'),
    path('textos/', views.listaTextos, name='listaTextos'),
    path('crearTexto/', views.crearTexto, name='crearTexto'),
    path('buscarUsuario/', views.buscarUsuario, name='buscarUsuario'),
    path('buscarTexto/', views.buscarTexto, name='buscarTexto'),
]

