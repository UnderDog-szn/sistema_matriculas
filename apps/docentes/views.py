from django.shortcuts import render, redirect
from .forms import DocenteForm

def crear_docente(request):
    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = DocenteForm()
    
    return render(request, 'docentes/inicio.html', {'form_docente': form})