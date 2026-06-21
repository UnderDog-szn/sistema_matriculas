from django.shortcuts import get_object_or_404, render, redirect
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


def actualizar_asignatura(request, pk):
    asignatura = get_object_or_404(asignaturas, pk=pk)
    if request.method == 'POST':
        form = AsignaturaForm(request.POST, instance=asignatura)
        if form.is_valid():
            form.save()
            return redirect('lista_asignaturas')
    else:
        form = AsignaturaForm(instance=asignatura)

    return render(
        request,
        'asignaturas/editar_asignatura.html',
        {'form': form, 'asignatura': asignatura}
    )


def eliminar_asignatura(request, pk):
    asignatura = get_object_or_404(asignaturas, pk=pk)
    if request.method == 'POST':
        asignatura.delete()
        return redirect('lista_asignaturas')
    return render(request, 'asignaturas/confirmar_eliminar.html', {'asignatura': asignatura})