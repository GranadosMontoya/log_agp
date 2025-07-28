from django.contrib.auth import authenticate, login, logout

from django.shortcuts import redirect, render
from django.views import View

class LoginView(View):
    template_name = 'User_Templates/login.html'  # Nombre de la plantilla de login
    def get(self, request):
        return render(request, self.template_name)
    # template_name = 'User/login.html'  # Nombre de la plantilla de login

    # def get(self, request):
    #     if request.user.is_authenticated:
    #         return redirect('User_app:home')  # Redirige si ya está autenticado
    #     return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        print("Te logueaste correctamente")

        if user is not None:
            login(request, user)
            # return redirect('User_app:home')  # Cambia 'dashboard' por la vista después de loguearse
        else:
            return render(request, self.template_name, {'error': 'Usuario o contraseña incorrectos'})