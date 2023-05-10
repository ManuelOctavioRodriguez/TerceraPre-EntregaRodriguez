from django import forms
from .models import Usuarios, Textos

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'
    
class TextosForm(forms.ModelForm):
    class Meta:
        model = Textos
        fields = '__all__'

class ComentariosForm(forms.Form):
    comentario = forms.CharField(max_length=240)
    autor = forms.ModelChoiceField(queryset=Usuarios.objects.all())
    texto = forms.ModelChoiceField(queryset=Textos.objects.all())