from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView,View, DeleteView
from apps.PC.models import Equipo,HistorialEquipo  # Ajusta si tu modelo está en otra app
from .forms import HistorialEquipoForm

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
        form = HistorialEquipoForm()  # 👈 Aquí instanciamos el form vacío
        return render(request, self.template_name, {'equipo': equipo, 'historial': historial,'form': form})
    

class AgregarHistorialView(LoginRequiredMixin, View):
    login_url = 'user:login'

    def post(self, request, serial):
        equipo = get_object_or_404(Equipo, serial=serial)
        form = HistorialEquipoForm(request.POST, request.FILES)

        if form.is_valid():
            historial = form.save(commit=False)
            historial.equipo = equipo
            historial.save()
            return redirect('pc:detalle_pc', serial=equipo.serial)

        # Si no es válido, lo regresamos al detalle con errores
        historial = HistorialEquipo.objects.filter(equipo=equipo).order_by('-fecha')
        return render(
            request,
            'detalle_pc.html',
            {
                'equipo': equipo,
                'historial': historial,
                'form': form
            }
        )


class EliminarEquipoView(LoginRequiredMixin, View):
    login_url = 'user:login'

    def post(self, request, serial):
        equipo = Equipo.objects.get(serial=serial)
        equipo.delete()
        return redirect(reverse_lazy('pc:pc_list'))  # 🔹 Ajusta al nombre de tu vista/lista