from django.urls import path
from . import views

urlpatterns = [
    path('crear-asignatura/', views.crear_asignatura, name='crear_asignatura'),
    path('lista-asignaturas/', views.lista_asignaturas, name='lista_asignaturas'),
]