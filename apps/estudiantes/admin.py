from django.contrib import admin
from .models import estudiantes
# Register your models here.


@admin.register(estudiantes)
class estudiantes(admin.ModelAdmin):
    list_display = ("nombre", "correo", "codigo", "sexo")
    search_fields = ("nombre", "codigo")
    ordering = ("nombre",)
