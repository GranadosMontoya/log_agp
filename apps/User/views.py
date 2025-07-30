from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('clave')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('user:home')  # Cambia esto a la ruta que quieres luego de login
        else:
            return render(request, 'user/login.html', {'mensaje': 'Credenciales inválidas'})
    elif request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('user:home')  # Redirige si ya está autenticado
        return render(request, 'user/login.html')

    return render(request, 'user/login.html')


def logout_view(request):
    logout(request)
    return redirect('user:login')



@login_required(login_url='user:login')
def bienvenida_view(request):
    return render(request, 'user/bienvenida.html')
