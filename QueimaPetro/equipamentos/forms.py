from django import forms
from database.models import Equipamento


class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = [
            "codigo",
            "nome",
            "fabricante",
            "numero_patrimonio",
            "status_operacional",
            "plataforma",
            "observacoes",
        ]

        labels = {
            "codigo": "Código do Equipamento",
            "nome": "Nome do Equipamento",
            "fabricante": "Fabricante",
            "numero_patrimonio": "Nº de Patrimônio",
            "status_operacional": "Status Operacional",
            "plataforma": "Plataforma",
            "observacoes": "Observações",
        }

        widgets = {
            "codigo": forms.TextInput(attrs={"class": "form-control"}),
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "fabricante": forms.TextInput(attrs={"class": "form-control"}),
            "numero_patrimonio": forms.TextInput(attrs={"class": "form-control"}),
            "status_operacional": forms.Select(attrs={"class": "form-control"}),
            "plataforma": forms.Select(attrs={"class": "form-control"}),
            "observacoes": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }
