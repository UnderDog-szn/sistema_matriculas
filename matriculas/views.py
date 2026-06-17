from django.shortcuts import render

def login(request):
    return render(request, 'login/base.html')

def inicio(request):
    return render(request, 'inicio_sistema.html')

def crear_docente(request):
    return render(request, 'docentes/inicio.html')