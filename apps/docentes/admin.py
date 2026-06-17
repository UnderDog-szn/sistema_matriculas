from django.contrib import admin
from .models import docentes


# Register your models here.
@admin.register(docentes)
class docentes(admin.ModelAdmin):
    list_display = ("nombre", "correo", "sexo")
    search_fields = ("nombre", "correo")
    ordering = ("nombre",)
