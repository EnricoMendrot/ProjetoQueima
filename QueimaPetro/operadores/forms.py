from django import forms
from database.models import Funcionario

class OperadorForm(forms.ModelForm):
    class Meta: #Classe de configuração
        model = Funcionario #modelo que vai referenciar
        fields = [
            'Nome',
            'Turno',
            'Cargo',
            'Permissao',
            'Supervisor',
            'Cidade',
            'Email',
            'Telefone',
            'CPF',
            'Setor',
            'ID_Plataforma',
            'Observacoes'
        ]

        widgets = {
            'Nome': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'Turno': forms.Select(attrs={
                'class': 'form-control'
            }),
            'Cargo': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'Supervisor': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'Cidade': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'Email': forms.EmailInput(attrs={
                'class': 'form-control',
            }),
            'Telefone': forms.TextInput(attrs={
                'class': 'forrm-control',
            }),
            'CPF': forms.TextInput(attrs={
                'class': 'form-control',
            }),''
            'Setor': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'ID_Plataforma': forms.Select(attrs={
                'class': 'form-control'
            }),
            'Permissao': forms.Select(attrs={
                'class': 'form-control'
            }),
            'Observacoes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        permissao = self.fields.get('Permissao')
        if permissao:
            permissao.choices = [('', '')] + list(permissao.choices)
