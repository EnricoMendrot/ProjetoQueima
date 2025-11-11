from django import forms
from database.models import Equipamento

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
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
                'placeholder': 'Informe o código do equipamento'
            }),
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
            'Numero_Patrimonio': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Informe o número de patrimônio'
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
            'Observacoes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Digite observações adicionais, se houver'
            }),
        }
