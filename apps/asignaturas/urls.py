from django.urls import path
from . import views

urlpatterns = [
    path('crear-asignatura/', views.crear_asignatura, name='crear_asignatura'),
]