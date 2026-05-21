from django.contrib import admin
from django.urls import path
from evaluaciones import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
]