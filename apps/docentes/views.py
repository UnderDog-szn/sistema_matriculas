from django.shortcuts import get_object_or_404, render, redirect
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

# ===== INICIO: Leer Docentes =====
def lista_docentes(request):
    docentes_lista = docentes.objects.all()
    return render(request, 'docentes/lista_docentes.html', {'docentes': docentes_lista})
# ===== FIN: Leer Docentes =====

# ===== INICIO: Actualizar Docente =====
def actualizar_docente(request, pk):
    docente = get_object_or_404(docentes, pk=pk)
    if request.method == 'POST':
        form = DocenteForm(request.POST, instance=docente)
        if form.is_valid():
            form.save()
            return redirect('lista_docentes')
    else:
        form = DocenteForm(instance=docente)
    return render(request, 'docentes/inicio.html', {'form_docente': form})
# ===== FIN: Actualizar Docente =====

# ===== INICIO: Eliminar Docente =====
def eliminar_docente(request, pk):
    docente = get_object_or_404(docentes, pk=pk)
    if request.method == 'POST':
        docente.delete()
        return redirect('lista_docentes')
    return render(request, 'docentes/confirmar_eliminar.html', {'docente': docente})
# ===== FIN: Eliminar Docente =====