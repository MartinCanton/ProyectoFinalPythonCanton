from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):

    first_name = forms.CharField(label="Nombre", max_length=15)
    last_name = forms.CharField(label="Apellido", max_length=15)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")


class UserEditForm(UserCreationForm):

    first_name = forms.CharField(label="Nombre", max_length=15)
    last_name = forms.CharField(label="Apellido", max_length=15)
    email = forms.EmailField()
    imagen = forms.ImageField()

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "imagen")