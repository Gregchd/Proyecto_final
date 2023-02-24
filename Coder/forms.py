from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProductosForm(forms.Form):
    nombre = forms.CharField()
    precio = forms.FloatField()
    codigo = forms.IntegerField()
    memoria = forms.CharField()
    camara = forms.CharField()
    ram = forms.CharField()
    bateria = forms.CharField()
    imagen = forms.ImageField()


class RegistroForm(UserCreationForm):
    nombre = forms.CharField(label="Nombre")
    apellido = forms.CharField(label="Apellido")
    correo = forms.EmailField(label="Correo")
    password1 = forms.CharField(
        label="Ingrese su contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Ingrese su contraseña otra vez", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "nombre", "apellido",
                  "correo", "password1", "password2"]
