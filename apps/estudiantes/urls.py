from django.urls import path
from . import views

urlpatterns = [
    path('crear-estudiante/', views.crear_estudiante, name='crear_estudiante'),
    path('', views.lista_estudiantes, name='lista_estudiantes'),
    path('<int:pk>/editar/', views.actualizar_estudiante, name='actualizar_estudiante'),
    path('<int:pk>/eliminar/', views.eliminar_estudiante, name='eliminar_estudiante'),
]