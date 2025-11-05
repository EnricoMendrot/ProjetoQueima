from django import forms
from database.models import Funcionario

class CadastroOperador(forms.ModelForm):
    class Meta: #Classe de configuração
        model = Funcionario #modelo que vai referenciar
        fields = [
            'Nome',
            'Cargo',
            'Email',
            'Telefone',
            'CPF',
            'Turno',
            'Empresa',
            'Setor',
            'Matricula',
            'ID_Plataforma'
        ] # Qual campo vai ser preenchido 