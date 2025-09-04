from django import forms
from .models import HistorialEquipo, Equipo

class HistorialEquipoForm(forms.ModelForm):
    class Meta:
        model = HistorialEquipo
        # Excluimos 'equipo' porque lo asignamos en la vista con get_object_or_404
        exclude = ['equipo', 'fecha']
        widgets = {
            'procesador': forms.TextInput(attrs={'class': 'form-control'}),
            'ram_gb': forms.TextInput(attrs={'class': 'form-control'}),
            'almacenamiento_gb': forms.TextInput(attrs={'class': 'form-control'}),
            'sistema_operativo': forms.TextInput(attrs={'class': 'form-control'}),
            'usuario_asignado': forms.TextInput(attrs={'class': 'form-control'}),
            'contraseña_asignado': forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'foto_historial': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre', 'serial', 'tipo', 'marca', 'modelo', 'empresa', 'foto_del_pc']