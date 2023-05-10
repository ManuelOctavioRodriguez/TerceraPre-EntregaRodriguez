from django import forms

class UsuariosForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    usuario = forms.CharField(max_length=20)
    pais = forms.CharField(max_length=20)
    correo = forms.EmailField()
    
class TextosForm(forms.Form):
    titulo = forms.CharField(max_length=40)
    texto = forms.CharField(max_length=480)
    image = forms.ImageField(upload_to='images/', blank=True)
    autor = forms.ForeignKey(UsuariosForm, on_delete=forms.CASCADE)

class Comentarios(forms.Form):
    comentario = forms.CharField(max_length=240)
    autor = forms.ForeignKey(UsuariosForm, on_delete=forms.CASCADE)
    texto = forms.ForeignKey(TextosForm, on_delete=forms.CASCADE)