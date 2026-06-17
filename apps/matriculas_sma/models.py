from django.db import models


# Create your models here.
class matriculas_sma(models.Model):
    codigo = models.CharField(max_length=20, primary_key=True, unique=True)
    estudiante = models.ForeignKey(
        "estudiantes.estudiantes",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="ID Estudiante",
    )

    asignatura = models.ForeignKey(
        "asignaturas.asignaturas",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="ID Asignatura",
    )

    fecha_de_matricula = models.DateField(
        auto_now_add=True,
    )

    class estado_matricula(models.TextChoices):
        Activa = "A", "Activa"
        Pendite = "P", "Pendiente"
        Cancelada = "C", "Cancelada"

    estado = models.CharField(
        max_length=10,
        blank=False,
        choices=estado_matricula,
        verbose_name="Estado de la matricula",
        default="Acttiva",
    )

    class Meta:
        verbose_name = "Matricula"
        verbose_name_plural = "Matriculas"

    def __str__(self):
        return f"{self.codigo}"
