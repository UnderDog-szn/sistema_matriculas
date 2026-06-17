from django.urls import path
from . import views

urlpatterns = [
    path('crear-estudiante/', views.crear_estudiante, name='crear_estudiante'),
]