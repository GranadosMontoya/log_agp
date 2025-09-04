from django.urls import path
from .views import PCView,DetallePCView, AgregarHistorialView, EliminarEquipoView, AgregarEquipoView
app_name = 'pc'
urlpatterns = [
    path('pc/', PCView.as_view(), name='pc_list'),
    path('pc/<str:serial>/', DetallePCView.as_view(), name='detalle_pc'),
    path('detalle/<str:serial>/agregar_historial/', AgregarHistorialView.as_view(), name='agregar_historial'),
    path('detalle/<str:serial>/eliminar/', EliminarEquipoView.as_view(), name='eliminar_equipo'),
    path('agregar_equipo/', AgregarEquipoView.as_view(), name='agregar_equipo'),

]
