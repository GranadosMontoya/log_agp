from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class PCView(LoginRequiredMixin, TemplateView):
    template_name = 'lista_pc.html'
    login_url = 'user:login'  # Redirección si no está logueado

    def get(self, request, *args, **kwargs):
        print("Sebas")  # Para confirmar que entra a la vista
        return super().get(request, *args, **kwargs)
