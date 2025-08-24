from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView,View
from apps.PC.models import Equipo,HistorialEquipo  # Ajusta si tu modelo está en otra app

class PCView(LoginRequiredMixin, ListView):
    paginate_by = 20  # Número de equipos por página
    model = Equipo
    template_name = 'lista_pc.html'
    context_object_name = 'equipos'  # Nombre con el que accedes a los objetos en la plantilla
    login_url = 'user:login'

    def get_queryset(self):
        return Equipo.objects.all().order_by('-fecha_registro')  # Por ejemplo, del más reciente al más antiguo

class DetallePCView(LoginRequiredMixin, View):
    login_url = 'user:login'
    template_name = 'detalle_pc.html'

    def get(self, request, serial):
        equipo = Equipo.objects.get(serial=serial)
        print(equipo)
        historial = HistorialEquipo.objects.filter(equipo=equipo).order_by('-fecha')
        return render(request, self.template_name, {'equipo': equipo, 'historial': historial})