from django.urls import path
from . import views

urlpatterns = [
    path('crear-docente/', views.crear_docente, name='crear_docente'),
    path('', views.lista_docentes, name='lista_docentes'),
    path('<str:pk>/editar/', views.actualizar_docente, name='actualizar_docente'),
    path('<str:pk>/eliminar/', views.eliminar_docente, name='eliminar_docente'),
]