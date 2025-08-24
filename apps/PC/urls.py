from django.urls import path
from .views import PCView,DetallePCView
app_name = 'pc'
urlpatterns = [
    path('pc/', PCView.as_view(), name='pc_list'),
    path('pc/<str:serial>/', DetallePCView.as_view(), name='detalle_pc'),
]
