from django.urls import path
from .views import *
app_name = 'empresas'
urlpatterns = [
    path('empresas/', EmpresaListView.as_view(), name='empresas_lista'),
    path('editar/<int:pk>/', editar_empresa, name="editar"),
    path('eliminar/<int:pk>/', eliminar_empresa, name="eliminar"),
    path("agregar/", agregar_empresa, name="agregar"),
]
