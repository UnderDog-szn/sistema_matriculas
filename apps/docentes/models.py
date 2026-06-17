from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


def validar_correo(correo):
    if "@" not in correo or not correo.endswith((".edu", ".co", ".com")):
        raise ValidationError(
            "El correo debe contener '@' y terminar en '.edu' '.co' '.com' "
        )


class docentes(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre completo")
    correo = models.CharField(
        max_length=100,
        validators=[validar_correo],
        unique=True,
        verbose_name="Correo electronico",
    )

    class sexo_docente(models.TextChoices):
        Hombre = "H", "Hombre"
        Mujer = "M", "Mujer"

    sexo = models.CharField(
        max_length=1,
        choices=sexo_docente,
        blank=False,
        default="H",
        verbose_name="Sexo",
    )

    class Meta:
        verbose_name = "Docente"
        verbose_name_plural = "Docentes"

    def __str__(self):
        return f"{self.nombre}"
