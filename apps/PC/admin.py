from django.contrib import admin
from .models import Equipo, HistorialEquipo

class HistorialEquipoInline(admin.TabularInline):
    model = HistorialEquipo
    extra = 1  # Cantidad de formularios vacíos por defecto

class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'serial', 'tipo', 'marca', 'modelo', 'fecha_registro')
    search_fields = ('nombre', 'serial', 'marca', 'modelo')
    list_filter = ('tipo', 'marca')
    inlines = [HistorialEquipoInline]  # Muestra el historial dentro del equipo

class HistorialEquipoAdmin(admin.ModelAdmin):
    list_display = ('equipo', 'fecha', 'usuario_asignado', 'ubicacion')
    search_fields = ('equipo__serial', 'usuario_asignado', 'ubicacion')
    list_filter = ('sistema_operativo', 'fecha')

admin.site.register(Equipo, EquipoAdmin)
admin.site.register(HistorialEquipo, HistorialEquipoAdmin)
