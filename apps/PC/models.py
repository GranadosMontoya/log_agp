from django.db import models
from ..Empresas.models import Empresa

# Opciones para el tipo de equipo
TIPO_EQUIPO_CHOICES = [
    ('PC', 'Computador de Escritorio'),
    ('LAPTOP', 'Portátil'),
    ('SERVIDOR', 'Servidor'),
    ('OTRO', 'Otro'),
]

class Equipo(models.Model):
    serial = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_EQUIPO_CHOICES)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    foto_del_pc = models.ImageField(upload_to='fotos_pc/', null=True, blank=True)
    empresa = models.ForeignKey('Empresas.Empresa', on_delete=models.CASCADE, null=True, blank=True)



    def __str__(self):
        return f"{self.nombre} - {self.serial}"

class HistorialEquipo(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='historial')
    fecha = models.DateTimeField(auto_now_add=True)

    procesador = models.CharField(max_length=100)
    ram_gb = models.CharField(max_length=100)
    almacenamiento_gb = models.CharField(max_length=100)
    sistema_operativo = models.CharField(max_length=100)
    usuario_asignado = models.CharField(max_length=100)
    contraseña_asignado = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    observaciones = models.TextField(blank=True, null=True)
    foto_historial = models.ImageField(upload_to='fotos_historial/', null=True, blank=True)  # Campo opcional de imagen
    class Meta:
        ordering = ['-fecha']  # Más recientes primero

    def __str__(self):
        return f"Historial de {self.equipo.serial} - {self.fecha.strftime('%Y-%m-%d')}"
