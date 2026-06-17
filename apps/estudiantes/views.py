from django.shortcuts import render, redirect
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