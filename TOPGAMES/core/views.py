from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    return render(request, 'core/index.html')

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
