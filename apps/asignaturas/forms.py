from django import forms
from .models import asignaturas

class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = asignaturas
        fields = '__all__'

        widgets = {
            'codigo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. MAT101'
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. Cálculo Diferencial'
            }),
            'docente': forms.Select(attrs={
                'class': 'form-select'
            }),
            'dia': forms.Select(attrs={
                'class': 'form-select'
            }),
            'hora': forms.TimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. 08:00',
                'type': 'time'
            }),
        }