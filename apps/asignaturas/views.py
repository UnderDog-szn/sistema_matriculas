from django.shortcuts import render, redirect
from .forms import AsignaturaForm

def crear_asignatura(request):
    if request.method == 'POST':
        form = AsignaturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = AsignaturaForm()
    return render(request, 'asignaturas/crear_asignatura.html', {'form': form})