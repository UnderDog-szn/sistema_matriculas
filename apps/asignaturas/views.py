from django.shortcuts import render, redirect
from .forms import AsignaturaForm
from .models import asignaturas

def crear_asignatura(request):
    ultimas_asignaturas = asignaturas.objects.all()[:5]

    if request.method == 'POST':
        form = AsignaturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_asignaturas')
    else:
        form = AsignaturaForm()
    return render(
        request,
        'asignaturas/crear_asignatura.html',
        {'form': form, 'ultimas_asignaturas': ultimas_asignaturas},
    )


def lista_asignaturas(request):
    asignaturas_lista = asignaturas.objects.all()
    return render(request, 'asignaturas/lista_asignaturas.html', {'asignaturas': asignaturas_lista})