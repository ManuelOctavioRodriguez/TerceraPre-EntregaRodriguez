from django.urls import path
from Common import views

urlpatterns = [
    path('', views.Home),
    path('Usuarios', views.Usuarios),
    path('Textos', views.Textos),
    path('Comentarios', views.Comentarios),
]
