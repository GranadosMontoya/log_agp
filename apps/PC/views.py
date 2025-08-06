from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from apps.PC.models import Equipo  # Ajusta si tu modelo está en otra app

class PCView(LoginRequiredMixin, ListView):
    model = Equipo
    template_name = 'lista_pc.html'
    context_object_name = 'equipos'  # Nombre con el que accedes a los objetos en la plantilla
    login_url = 'user:login'

    def get_queryset(self):
        return Equipo.objects.all().order_by('-fecha_registro')  # Por ejemplo, del más reciente al más antiguo

