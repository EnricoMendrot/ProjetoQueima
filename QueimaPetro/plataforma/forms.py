from django import forms
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
            'Nome': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'Localizacao': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'Tipo': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'DataComissionamento': forms.TextInput(attrs={
                'class': 'form-control',
            }),
             'Status': forms.Select(attrs={
                'class': 'form-control'
            }),
            'Supervisor': forms.Select(attrs={
                'class': 'form-control'
            }),
            'ResponsavelTecnico': forms.Select(attrs={
                'class': 'form-control'
            }),
            'OperadorPrincipal': forms.Select(attrs={
                'class': 'form-control'
            }),
            'EquipamentoManutencao': forms.Select(attrs={
                'class': 'form-control'
            }),
            'Observacoes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
            }),
        }