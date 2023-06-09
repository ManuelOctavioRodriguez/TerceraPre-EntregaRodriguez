from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate

from Perfiles.models import Avatar
from Perfiles.forms import UserRegisterForm, UserUpdateForm, AvatarFormulario

def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()  
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:  
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name='Perfiles/registro.html',
        context={'form': formulario},
    )
    
def login_view(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get('username')
            password = data.get('password')
            user = authenticate(username=usuario, password=password)
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                url_exitosa = reverse('inicio')
                return redirect(url_exitosa)
    else:  
        form = AuthenticationForm()
    return render(
        request=request,
        template_name='Perfiles/login.html',
        context={'form': form},
    )
    
class CustomLogoutView(LogoutView):
   template_name = 'Perfiles/logout.html'
   
