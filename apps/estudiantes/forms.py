from django import forms
from .models import estudiantes

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = estudiantes
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. Juan Pérez'
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com'
            }),
            'codigo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. 202500123'
            }),
            'sexo': forms.Select(attrs={
                'class': 'form-select'
            }),
        }