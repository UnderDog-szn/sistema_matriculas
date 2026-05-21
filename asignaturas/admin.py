from django.contrib import admin
from .models import asignaturas
# Register your models here.


@admin.register(asignaturas)
class asignaturas(admin.ModelAdmin):
    list_display = ("nombre", "dia_de_clase", "hora", "docente", "codigo")
    search_fields = ("nombre", "codigo")
    ordering = ("nombre",)
