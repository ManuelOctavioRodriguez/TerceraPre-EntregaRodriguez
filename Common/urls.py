from django.urls import path
from Common.views import Home, Usuarios, Textos, Comentarios

urlpatterns = [
    path('', Home),
    path('Usuarios/', Usuarios),
    path('Textos/', Textos),
    path('Comentarios/', Comentarios),
]
