from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, update_session_auth_hash
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .forms import RegistroClienteForm


def index(request):
    return render(request, 'core/index.html')

def registro(request):
    if request.method == 'post':
        form = RegistroClienteForm(request.post)
        if form.is_valid():
            form.save()
        return render(request,'core/registro.html')
    else:
        form = RegistroClienteForm()
    contexto = {
        'form': form,
        'cliente': request.user
    }
    return render(request,'core/registro.html', contexto)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')
    return render(request, 'core/login.html')

def carrito(request):
    return render(request, 'core/carrito.html')


@login_required
def modificar_perfil(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')

        user = request.user
        user.username = username

        if password and password == confirm_password:
            user.set_password(password)
            update_session_auth_hash(request, user) 

        user.save()
        messages.success(request, 'Perfil actualizado exitosamente.')
        return redirect('modificar_perfil')

    return render(request, 'core/moduser.html', {'user': request.user})
