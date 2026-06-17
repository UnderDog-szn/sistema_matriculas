from django.urls import path
from . import views

urlpatterns = [
    path('crear-estudiante/', views.crear_estudiante, name='crear_estudiante'),
    path('lista-estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),
]