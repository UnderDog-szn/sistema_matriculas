from django.shortcuts import render, redirect
from .forms import DocenteForm
from .models import docentes

def crear_docente(request):
    ultimos_docentes = docentes.objects.all()[:5]

    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_docentes')
    else:
        form = DocenteForm()
    
    return render(
        request,
        'docentes/inicio.html',
        {'form_docente': form, 'ultimos_docentes': ultimos_docentes},
    )


def lista_docentes(request):
    docentes_lista = docentes.objects.all()
    return render(request, 'docentes/lista_docentes.html', {'docentes': docentes_lista})