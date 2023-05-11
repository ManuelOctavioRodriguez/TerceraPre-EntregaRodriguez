from django import forms
from .models import Usuarios, Textos, Comentarios

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'
    
class TextosForm(forms.ModelForm):
    class Meta:
        model = Textos
        fields = '__all__'

class ComentariosForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = '__all__'