from django.contrib import admin
from .models import matriculas_sma
# Register your models here.


@admin.register(matriculas_sma)
class matriculas_sma(admin.ModelAdmin):
    list_display = (
        "codigo",
        "estudiante",
        "asignatura_id",
        "fecha_de_matricula",
        "estado",
    )
    search_fields = ("codigo",)
    ordering = ("codigo",)
