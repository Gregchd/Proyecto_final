from django.urls import path
from Coder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('home/', home, name="home"),

    # CRUD
    path('productos/lista', ProductoLista.as_view(), name="Ver productos"),
    path('productos/nuevo', ProductoCrear, name="Crear productos"),
    path('productos/borrar/<int:pk>',
         ProductoBorrar.as_view(), name="Borrar productos"),
    path('productos/editar/<int:pk>',
         ProductoEditar.as_view(), name="Editar productos"),

    # Registro
    path('registro/', registro, name="registro"),
    path('login/', logeo, name="login"),
    path('logout/', LogoutView.as_view(template_name="Coder/auth/logout.html"), name="logout"),

    # Busqueda
    path('productos/b_producto/', b_producto, name="b_producto"),
    path('productos/v_busqueda/', v_busqueda, name="v_busqueda"),

    # about
    path('about/', about, name="about"),
]
