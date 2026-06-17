from django.contrib import admin
from django.urls import path, include
from matriculas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('inicio/', views.inicio, name='inicio'),
    path('docentes/', include('apps.docentes.urls')),
    path('estudiantes/', include('apps.estudiantes.urls')),
    path('asignaturas/', include('apps.asignaturas.urls')),
]