from django.db import models

# Create your models here.


class asignaturas(models.Model):
    nombre = models.CharField(max_length=100)
    docente = models.ForeignKey(
        "docentes.docentes",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Docente",
    )

    codigo = models.CharField(
        max_length=20, primary_key=True, verbose_name="Codigo", unique=True
    )

    class dia(models.TextChoices):
        Lunes = "Lunes"
        Martes = "Martes"
        Miercoles = "Miercoles"
        Jueves = "Jueves"
        Viernes = "Viernes"

    dia_de_clase = models.CharField(
        max_length=9, blank=False, default="Lunes", choices=dia, verbose_name="Dia"
    )

    hora = models.TimeField(null=True, verbose_name="Hora de la clase")

    class Meta:
        verbose_name = "Asignatura"
        verbose_name_plural = "Asignaturas"

    def __str__(self):
        return f"{self.nombre}"
