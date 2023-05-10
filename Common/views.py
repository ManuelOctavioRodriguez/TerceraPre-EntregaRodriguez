from .models import Usuarios, Textos, Comentarios
from .forms import UsuariosForm, TextosForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

def Index(request):
    contexto = {}
    return render(request, template_name='Common/Inicio.html', context=contexto)

def listaUsuarios(request):
    contexto = {
        "usuarios": Usuarios.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='Common/usuarios.html',
        context=contexto,
    )
    return http_response

def listaTextos(request):
    contexto = {
        "textos": Textos.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='Common/textos.html',
        context=contexto,
    )
    return http_response

def crearUsuario(request):
    if request.method == "POST":
        formulario = UsuariosForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            apellido = data["apellido"]
            pais = data["pais"]
            correo = data["correo"]
            usuario = Usuarios(nombre=nombre, apellido=apellido, pais=pais, correo=correo)
            usuario.save()  

            url_exitosa = reverse('listaUsuarios') 
            return redirect(url_exitosa)
        
        else: 
            formulario = UsuariosForm()
            http_response = render(
            request=request,
            template_name='Common/crearUsuario.html',
            context={'formulario': formulario}
        )
        return http_response
    
def crearTexto(request):
    if request.method == "POST":
        formulario = TextosForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            titulo = data["titulo"]
            texto = data["texto"]
            image = data["image"]
            autor = data["autor"]
            texto = Textos(titulo=titulo, texto=texto, image=image, autor=autor)
            texto.save()  

            url_exitosa = reverse('listaTextos') 
            return redirect(url_exitosa)
        
        else: 
            formulario = TextosForm()
            http_response = render(
            request=request,
            template_name='Common/crearTexto.html',
            context={'formulario': formulario}
        )
        return http_response