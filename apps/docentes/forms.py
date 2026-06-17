from django import forms
from .models import docentes

class DocenteForm(forms.ModelForm):
    class Meta:
        model = docentes
        fields = ['nombre', 'correo', 'sexo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Juan Pérez'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@unicualquiera.edu'}),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
        }