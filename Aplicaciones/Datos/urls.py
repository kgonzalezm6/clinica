from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('registrarPaciente/', views.registrarPaciente),
    path('eliminarPaciente/<DPI>',views.eliminarPaciente),
    path('edicionPaciente/<DPI>',views.edicionPaciente),
    path('editarPaciente/',views.editarPaciente),
    path('registrarMedico/',views.registrarMedico),
    path('eliminarMedico/<Numero_Colegiado>',views.eliminarMedico),
    path('edicionMedico/<Numero_Colegiado>',views.edicionMedico),
    path('editarMedico/',views.editarMedico)
    
    
    
]
