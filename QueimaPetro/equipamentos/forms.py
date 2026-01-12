from django import forms
from database.models import Equipamento
from operadores.forms import OperadorForm

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = [
            'Codigo',
            'Nome',
            'Fabricante',
            'Numero_Patrimonio',
            'Status_Operacional',
            'Plataforma',
            'Observacoes',
        ]

        labels = {
            'Codigo': 'Código do Equipamento',
            'Nome': 'Nome do Equipamento',
            'Fabricante': 'Fabricante',
            'Numero_Patrimonio': 'Nº de Patrimônio',
            'Status_Operacional': 'Status Operacional',
            'Plataforma': 'Plataforma',
            'Observacoes': 'Observações',
        }

        widgets = {
            'Codigo': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'Nome': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'Fabricante': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'Numero_Patrimonio': forms.TextInput(attrs={
                'class': 'form-control',
            }),
             'Status_Operacional': forms.Select(attrs={
                'class': 'form-control'
            }),
            'Plataforma': forms.Select(attrs={
                'class': 'form-control'
            }),
            'Observacoes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
            }),
        }
