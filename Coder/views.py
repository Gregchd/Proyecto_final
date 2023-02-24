from django.shortcuts import render


from Coder.models import *
from Coder.forms import *

from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    return render(request, "Coder/home.html")


# Registro
def registro(request):
    if request.method == 'POST':
        miForm = RegistroForm(request.POST)

        if miForm.is_valid():
            miForm.save()

            return render(request, "Coder/home.html")

    else:
        miForm = RegistroForm()

    return render(request, "Coder/auth/registro.html", {"miForm": miForm})

# Login


def logeo(request):
    if request.method == "POST":
        # obtener los datos que están en el formulario
        miForm = AuthenticationForm(request, data=request.POST)

        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            contra = miForm.cleaned_data.get("password")

            miUsuario = authenticate(username=usuario, password=contra)

            if miUsuario:
                login(request, miUsuario)
                mensaje = f"Bienvenido {miUsuario}"

                return render(request, "Coder/home.html", {"mensaje": mensaje})

        else:
            mensaje = f"Error. Ingresaste mal los datos."
            return render(request, "Coder/home.html", {"mensaje": mensaje})

    else:
        miForm = AuthenticationForm()

    return render(request, "Coder/auth/login.html", {"miForm": miForm})


# Productos

class ProductoLista(ListView):
    model = Productos
    template_name = "Coder/productos/r_productos.html"


def ProductoCrear(request):
    if request.method == 'POST':
        miForm = ProductosForm(request.POST, request.FILES)

        if miForm.is_valid():

            infoDic = miForm.cleaned_data
            producto = Productos(nombre=infoDic["nombre"],
                                 precio=infoDic["precio"],
                                 codigo=infoDic["codigo"],
                                 memoria=infoDic["memoria"],
                                 camara=infoDic["camara"],
                                 ram=infoDic["ram"],
                                 bateria=infoDic["bateria"],
                                 imagen=infoDic["imagen"],)

            producto.save()

            return render(request, "Coder/home.html")
    else:
        miForm = ProductosForm()

    return render(request, "Coder/productos/c_productos.html", {"form_productos": miForm})


""" class ProductoCrear(LoginRequiredMixin, CreateView):
    model = Productos
    template_name = "Coder/productos/c_productos.html"
    fields = ["nombre", "precio", "codigo",
              "camara", "memoria", "ram", "bateria", "imagen"]
    success_url = "/Coder/productos/lista" """


class ProductoBorrar(LoginRequiredMixin, DeleteView):
    model = Productos
    template_name = "Coder/productos/d_productos.html"
    success_url = "/Coder/productos/lista"


class ProductoEditar(LoginRequiredMixin, UpdateView):
    model = Productos
    template_name = "Coder/productos/u_productos.html"
    fields = ["nombre", "precio", "codigo",
              "camara", "memoria", "ram", "bateria", "imagen"]
    success_url = "/Coder/productos/lista"


# BUSQUEDA
def b_producto(request):
    return render(request, "Coder/productos/b_productos.html")


def v_busqueda(request):
    if request.method == "GET":
        camara = request.GET["camara"]
        producto = Productos.objects.filter(camara__icontains=camara)

        return render(request, "Coder/productos/v_busqueda.html", {"camara": camara, "resultado": producto})

    return render(request, "Coder/productos/v_busqueda.html")


def about(request):
    return render(request, "Coder/about.html")
