from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from .models import Empresa

# Create your views here.

class EmpresaListView(ListView):
    model = Empresa
    template_name = "lista_empresas.html"
    context_object_name = "empresas"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Empresa.objects.filter(nombre__icontains=query).order_by("nombre")
        return Empresa.objects.all().order_by("nombre")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "")
        return context
    

def editar_empresa(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == "POST":
        empresa.nombre = request.POST.get("nombre")
        empresa.identificacion = request.POST.get("identificacion")
        empresa.direccion = request.POST.get("direccion")
        empresa.telefono = request.POST.get("telefono")
        empresa.email = request.POST.get("email")
        empresa.contacto = request.POST.get("contacto")
        empresa.save()
    return redirect("empresas:empresas_lista")


def eliminar_empresa(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == "POST":
        empresa.delete()
    return redirect("empresas:empresas_lista")


def agregar_empresa(request):
    if request.method == "POST":
        Empresa.objects.create(
            nombre=request.POST.get("nombre"),
            identificacion=request.POST.get("identificacion"),
            direccion=request.POST.get("direccion"),
            telefono=request.POST.get("telefono"),
            email=request.POST.get("email"),
            contacto=request.POST.get("contacto")
        )
    return redirect("empresas:empresas_lista")