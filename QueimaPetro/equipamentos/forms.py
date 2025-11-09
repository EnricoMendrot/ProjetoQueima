from django import forms
from database.models import Equipamento

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = [
            'Nome',
            'Tipo',
            'Fabricante',
            'Modelo',
            'Status_Operacional',
            'Plataforma',
            'Funcionario',
        ]

        labels = {
            'Nome': 'Nome do Equipamento',
            'Tipo': 'Tipo de Equipamento',
            'Fabricante': 'Fabricante',
            'Modelo': 'Modelo',
            'Status_Operacional': 'Status Operacional',
            'Plataforma': 'Plataforma',
            'Funcionario': 'Funcionário Responsável',
        }

        widgets = {
            'Nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome do equipamento'
            }),
            'Tipo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Informe o tipo'
            }),
            'Fabricante': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Informe o fabricante'
            }),
            'Modelo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Informe o modelo'
            }),
            'Status_Operacional': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Ativo, Inativo, Em Manutenção'
            }),
            'Plataforma': forms.Select(attrs={
                'class': 'form-control'
            }),
            'Funcionario': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
