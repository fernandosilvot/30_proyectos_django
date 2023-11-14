from django.urls import path
from . import views

urlpatterns = [
    path('', views.PaginaPrincipal, name='PaginaPrincipal'),
    path('Estudio/', views.Estudio, name='Estudio'),
    path('proyectos/', views.Proyectos, name='Proyectos'),
]
