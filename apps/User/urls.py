from django.urls import path, re_path
from . import views

app_name = 'user'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    re_path('logout/', views.logout_view, name='logout'),
    path('', views.bienvenida_view, name='home')

]
