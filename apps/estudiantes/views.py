from django.shortcuts import render, redirect
from .forms import EstudianteForm

def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = EstudianteForm()
    return render(request, 'estudiantes/crear_estudiante.html', {'form': form})