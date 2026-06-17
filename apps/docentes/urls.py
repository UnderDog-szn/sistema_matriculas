from django.urls import path
from . import views

urlpatterns = [
    path('crear-docente/', views.crear_docente, name='crear_docente'),
]