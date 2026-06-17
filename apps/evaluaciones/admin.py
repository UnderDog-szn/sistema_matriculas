from django.contrib import admin
from .models import Actividad, Criterio, Calificacion, NotaFinal

admin.site.register(Actividad)
admin.site.register(Criterio)
admin.site.register(Calificacion)
admin.site.register(NotaFinal)