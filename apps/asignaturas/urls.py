from django.urls import path
from . import views

urlpatterns = [
    path('crear-asignatura/', views.crear_asignatura, name='crear_asignatura'),
    path('', views.lista_asignaturas, name='lista_asignaturas'),
    path('<str:pk>/editar/', views.actualizar_asignatura, name='actualizar_asignatura'),
    path('<str:pk>/eliminar/', views.eliminar_asignatura, name='eliminar_asignatura'),
]