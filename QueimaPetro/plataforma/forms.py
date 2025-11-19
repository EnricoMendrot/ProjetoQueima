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