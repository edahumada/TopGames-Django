from django.urls import path
from .views import index, login, carrito

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('carrito/', carrito, name='carrito'),
]
