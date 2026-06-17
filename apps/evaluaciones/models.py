from django.db import models

# ── ACTIVIDAD ──────────────────────────────────────────
class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_entrega = models.DateField()
    docente = models.ForeignKey(
        "docentes.docentes",
        on_delete=models.SET_NULL,
        null=True
    )
    
    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"

    def __str__(self):
        return self.nombre


# ── CRITERIO ───────────────────────────────────────────
class Criterio(models.Model):
    descripcion = models.CharField(max_length=200)
    porcentaje = models.FloatField()
    actividad = models.ForeignKey(
        Actividad,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Criterio"
        verbose_name_plural = "Criterios"

    def __str__(self):
        return self.descripcion


# ── CALIFICACION ───────────────────────────────────────
class Calificacion(models.Model):
    estudiante = models.ForeignKey(
        "estudiantes.estudiantes",
        on_delete=models.CASCADE
    )
    criterio = models.ForeignKey(
        Criterio,
        on_delete=models.CASCADE
    )
    puntaje = models.FloatField()

    class Meta:
        verbose_name = "Calificación"
        verbose_name_plural = "Calificaciones"

    def __str__(self):
        return f"{self.estudiante} - {self.criterio}"


# ── NOTA FINAL ─────────────────────────────────────────
class NotaFinal(models.Model):
    estudiante = models.OneToOneField(
        "estudiantes.estudiantes",
        on_delete=models.CASCADE
    )
    actividad = models.ForeignKey(
        Actividad,
        on_delete=models.CASCADE
    )
    nota_calculada = models.FloatField()

    class Meta:
        verbose_name = "Nota Final"
        verbose_name_plural = "Notas Finales"

    def __str__(self):
        return f"{self.estudiante} - {self.nota_calculada}"