from django.shortcuts import get_object_or_404, render, redirect
from .forms import EstudianteForm
from .models import estudiantes

def crear_estudiante(request):
    ultimos_estudiantes = estudiantes.objects.all()[:5]

    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm()

    return render(
        request,
        'estudiantes/crear_estudiante.html',
        {'form': form, 'ultimos_estudiantes': ultimos_estudiantes},
    )


def lista_estudiantes(request):
    estudiantes_lista = estudiantes.objects.all()
    return render(request, 'estudiantes/lista_estudiantes.html', {'estudiantes': estudiantes_lista})


def actualizar_estudiante(request, pk):
    estudiante = get_object_or_404(estudiantes, pk=pk)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm(instance=estudiante)

    return render(
        request,
        'estudiantes/editar_estudiante.html',
        {'form': form, 'estudiante': estudiante}
    )


def eliminar_estudiante(request, pk):
    estudiante = get_object_or_404(estudiantes, pk=pk)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('lista_estudiantes')
    return render(request, 'estudiantes/confirmar_eliminar.html', {'estudiante': estudiante})