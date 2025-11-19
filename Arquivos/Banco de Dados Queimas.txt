from django.db import models

# Create your models here.

class Plataforma(models.Model):
    ID_Plataforma = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=100)
    Localizacao = models.CharField(max_length=200)
    Tipo = models.CharField(max_length=100)
    DataComissionamento = models.DateTimeField()
    DataInspecao = models.DateTimeField()
    Status = models.CharField(max_length=100)
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
    StatusComunicacao = models.CharField(max_length=20)

    def __str__(self):
        return f"Ocorrência {self.ID_OcorrenciaQueima} - {self.ClassificacaoQueima}"


class Equipamento(models.Model):
    ID_Equipamento = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=100)
    Tipo = models.CharField(max_length=100)
    Fabricante = models.CharField(max_length=100, null=True, blank=True)
    Status_Operacional = models.CharField(max_length=50)

    Codigo = models.CharField(max_length=50, null=True, blank=True)
    Modelo = models.CharField(max_length=100, blank=True, null=True)
    Numero_Patrimonio = models.CharField(max_length=50, blank=True, null=True)
    Observacoes = models.TextField(blank=True, null=True)

    Plataforma = models.ForeignKey(
        'Plataforma',
        on_delete=models.SET_NULL,
        null=True,
        db_column='ID_Plataforma'
    )
    Funcionario = models.ForeignKey(
        'Funcionario',
        on_delete=models.CASCADE,
        db_column='ID_Funcionario'
    )

    def __str__(self):
        return f"{self.Nome} - {self.Tipo}"
