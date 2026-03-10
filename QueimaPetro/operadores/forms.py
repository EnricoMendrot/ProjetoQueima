from django import forms
from database.models import Funcionario


class OperadorForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = [
            "nome",
            "turno",
            "cargo",
            "permissao",
            "supervisor",
            "cidade",
            "email",
            "telefone",
            "cpf",
            "setor",
            "plataforma",
            "observacoes",
        ]

        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "turno": forms.Select(attrs={"class": "form-control"}),
            "cargo": forms.TextInput(attrs={"class": "form-control"}),
            "permissao": forms.Select(attrs={"class": "form-control"}),
            "supervisor": forms.TextInput(attrs={"class": "form-control"}),
            "cidade": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "telefone": forms.TextInput(attrs={"class": "form-control"}),
            "cpf": forms.TextInput(attrs={"class": "form-control"}),
            "setor": forms.TextInput(attrs={"class": "form-control"}),
            "plataforma": forms.Select(attrs={"class": "form-control"}),
            "observacoes": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Coloca uma opção vazia no começo do select de permissão
        permissao = self.fields.get("permissao")
        if permissao:
            permissao.choices = [("", "---------")] + list(permissao.choices)
