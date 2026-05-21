from django.db import models
from django.core.exceptions import ValidationError


def validar_correo(correo):
    if "@" not in correo or not correo.endswith((".edu", ".co", ".com")):
        raise ValidationError(
            "El correo debe contener '@' y terminar en .edu, .co, .com"
        )


# Create your models here.
class estudiantes(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre completo")
    correo = models.CharField(
        max_length=100,
        verbose_name="Correo electronico",
        validators=[validar_correo],
        unique=True,
    )
    codigo = models.CharField(
        max_length=100, verbose_name="Codigo estudiantil", unique=True
    )

    class sexo_estudiante(models.TextChoices):
        Hombre = "H", "Hombre"
        Mujer = "M", "Mujer"

    sexo = models.CharField(
        max_length=1,
        choices=sexo_estudiante,
        blank=False,
        default="H",
        verbose_name="Sexo",
    )

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

    def __str__(self):
        return f"{self.nombre}"
