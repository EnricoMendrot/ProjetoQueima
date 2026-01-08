from django import forms
from django.forms.widgets import DateInput
from database.models import Plataforma

class PlataformaForm(forms.ModelForm):
    class Meta:
        model = Plataforma
        fields = [
            'Nome',
            'Localizacao',
            'Tipo',
            'DataComissionamento',
            'DataInspecao',
            'Status',
            'Supervisor',
            'ResponsavelTecnico',
            'OperadorPrincipal',
            'Observacoes',
            'EquipeManutencao',
        ]

        widgets = {
            'DataInspecao': DateInput(
                attrs={
                    'type': 'date',       
                    'class': 'form-control', 
                    'placeholder': 'dd/mm/aaaa',
                },
                format='%Y-%m-%d'),

            # Se quiser fazer o mesmo para DataComissionamento:
            'DataComissionamento': DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                },
            ),

            'Nome': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'Localizacao': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'Tipo': forms.Select(attrs={
                'class': 'form-control',
            }),
             'Status': forms.Select(attrs={
                'class': 'form-control'
            }),
            'Supervisor': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'ResponsavelTecnico': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'OperadorPrincipal': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'EquipamentoManutencao': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'Observacoes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
            }),
        }