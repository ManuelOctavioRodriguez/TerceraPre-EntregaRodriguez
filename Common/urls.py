from django.urls import path
from Common.views import Home, Usuarios, Textos, Comentarios, Index

urlpatterns = [
    path(' ', Index),
    path('Home/', Home),
    path('Usuarios/', Usuarios),
    path('Textos/', Textos),
    path('Comentarios/', Comentarios),
]
