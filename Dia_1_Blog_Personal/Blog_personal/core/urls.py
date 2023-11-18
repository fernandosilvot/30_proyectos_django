from django.urls import path
from . import views

urlpatterns = [
    path('', views.PaginaPrincipal, name='PaginaPrincipal'),
    path('Ingresar/', views.Ingresar, name='Ingresar'),
    path('Registrar/', views.Registrar, name='Registrar'),
    path('Logout/', views.Logout, name='Logout'),
    path('Perfil/<int:id>', views.PerfilUsuario, name='Perfil'),
]
