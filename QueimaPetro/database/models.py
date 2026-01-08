from django.db import models

# Create your models here.

class Plataforma(models.Model):
    STATUS_CHOICES = [
        ('ativa', 'Ativa'),
        ('inativa', 'Inativa'),
    ]
    Status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES
    )
    TIPO_PLATAFORMA_CHOICES = [
        ('fixa', 'Fixas'),
        ('autoelevável', 'Autoelevável'),
        ('semissubmersível', 'Semissubmersível'),
        ('navio-sonda', 'Navio-Sonda'),
        ('FPSO', 'FPSO'),
        ('TLWP/TLP', 'TLWP/TLP'),
    ] 

    Tipo = models.CharField(
        max_length=100, 
        choices=TIPO_PLATAFORMA_CHOICES
    )

    ID_Plataforma = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=100)
    Localizacao = models.CharField(max_length=200)
    DataComissionamento = models.DateTimeField(
        blank=False,
        null=False,
    )
    DataInspecao = models.DateTimeField()
    Supervisor = models.CharField(max_length=100)
    ResponsavelTecnico = models.CharField(max_length=100)
    OperadorPrincipal = models.CharField(max_length=100)
    EquipeManutencao = models.CharField(max_length=100)
    Observacoes = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.Nome


class Funcionario(models.Model):
    ID_Funcionario = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=100)
    Cargo = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100, unique=True)
    Telefone = models.CharField(max_length=15, unique=True)
    CPF = models.CharField(max_length=15, unique=True)
    Turno = models.CharField(max_length=50)
    Empresa = models.CharField(max_length=100)
    Setor = models.CharField(max_length=100)
    Matricula = models.CharField(max_length=20, unique=True)
    ID_Plataforma = models.ForeignKey(
        Plataforma,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.Nome} ({self.Cargo})"


class OcorrenciaQueima(models.Model):
    ID_OcorrenciaQueima = models.AutoField(primary_key=True)
    ID_Plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE)
    ID_Funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    Responsavel = models.CharField(max_length=100)
    Data_Hora = models.DateTimeField()
    Vazao = models.DecimalField(max_digits=10, decimal_places=2)
    Gas = models.CharField(max_length=100)
    ClassificacaoQueima = models.CharField(max_length=50)
    statuscomunicacao = models.CharField(max_length=20)

    def __str__(self):
        return f"Ocorrência {self.ID_OcorrenciaQueima} - {self.ClassificacaoQueima}"


class Equipamento(models.Model):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
        ('manutencao', 'Em Manutenção'),
    ]

    Status_Operacional = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )

    ID_Equipamento = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=100)
    Fabricante = models.CharField(max_length=100, null=True, blank=True)
    Codigo = models.CharField(max_length=50, null=True, blank=True)
    Numero_Patrimonio = models.CharField(max_length=50, blank=True, null=True)
    Observacoes = models.TextField(blank=True, null=True)

    Plataforma = models.ForeignKey(
        'Plataforma',
        on_delete=models.SET_NULL,
        null=True,
        db_column='ID_Plataforma'
    )

