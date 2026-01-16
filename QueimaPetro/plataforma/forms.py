from django import forms
from django.forms.widgets import DateInput
from database.models import Plataforma


class PlataformaForm(forms.ModelForm):
    class Meta:
        model = Plataforma
        fields = [
            "nome",
            "localizacao",
            "tipo",
            "status",
            "data_comissionamento",
            "data_inspecao",
            "supervisor",
            "responsavel_tecnico",
            "operador_principal",
            "equipe_manutencao",
            "observacoes",
        ]

        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),

            "localizacao": forms.TextInput(attrs={"class": "form-control"}),

            "tipo": forms.Select(attrs={"class": "form-control"}),

            "status": forms.Select(attrs={"class": "form-control"}),

            "data_comissionamento": DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                },
                format="%Y-%m-%d",
            ),

            "data_inspecao": DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                },
                format="%Y-%m-%d",
            ),

            "supervisor": forms.TextInput(attrs={"class": "form-control"}),

            "responsavel_tecnico": forms.TextInput(attrs={"class": "form-control"}),

            "operador_principal": forms.TextInput(attrs={"class": "form-control"}),

            "equipe_manutencao": forms.TextInput(attrs={"class": "form-control"}),

            "observacoes": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 2,
                }
            ),
        }
