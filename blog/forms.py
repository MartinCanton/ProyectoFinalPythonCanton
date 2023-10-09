from django import forms
from blog.models import Articulo, Comentario, Mensaje


class ArtForm(forms.ModelForm):

    class Meta:
        model = Articulo
        fields = ['fecha', 'titulo', 'subtitulo', 'cuerpo', 'imagen']


class BuscarArtForm(forms.Form):
    titulo = forms.CharField(min_length=3, max_length=20)


class ComForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ['date', 'titulo', 'comentar', 'articulo']

class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Mensaje
        fields = ['nombre', 'email', 'mensaje']        