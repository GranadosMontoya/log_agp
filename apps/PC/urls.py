from django.urls import path
from .views import PCView
app_name = 'pc'
urlpatterns = [
    path('pc/', PCView.as_view(), name='pc_view'),
]
