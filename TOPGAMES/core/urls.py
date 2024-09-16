from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index, login, carrito, modificar_perfil

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('carrito/', carrito, name='carrito'),
    path('modificar_perfil/', modificar_perfil, name='modificar_perfil'),
