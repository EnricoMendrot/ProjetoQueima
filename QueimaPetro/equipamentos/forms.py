from django import forms
from database.models import Equipamento

class EquipamentoForm(forms.ModelForm):
    class Meta:
        fields = [
            'Codigo',
            'Nome',
            'Tipo',
            'Fabricante',
            'Modelo',
            'Numero_Patrimonio',
            'Status_Operacional',
            'Plataforma',
            'Funcionario',
            'Observacoes',
        ]

        labels = {
            'Codigo': 'Código do Equipamento',
            'Nome': 'Nome do Equipamento',
            'Tipo': 'Tipo de Equipamento',
            'Fabricante': 'Fabricante',
            'Modelo': 'Modelo',
            'Numero_Patrimonio': 'Nº de Patrimônio',
            'Status_Operacional': 'Status Operacional',
            'Plataforma': 'Plataforma',
            'Funcionario': 'Funcionário Responsável',
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
            'Funcionario': forms.Select(attrs={
                'class': 'form-control'
            }),
            'Observacoes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
            }),
        }
