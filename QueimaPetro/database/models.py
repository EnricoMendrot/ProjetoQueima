from django.db import models


class Plataforma(models.Model):
    class Status(models.TextChoices):
        ATIVA = "ativa", "Ativa"
        INATIVA = "inativa", "Inativa"

    class TipoPlataforma(models.TextChoices):
        FIXA = "fixa", "Fixa"
        AUTOELEVAVEL = "autoelevavel", "Autoelevável"
        SEMISSUBMERSIVEL = "semissubmersivel", "Semissubmersível"
        NAVIO_SONDA = "navio_sonda", "Navio-Sonda"
        FPSO = "fpso", "FPSO"
        TLWP_TLP = "tlwp_tlp", "TLWP/TLP"

    id = models.AutoField(primary_key=True)

    nome = models.CharField(max_length=100, unique=True, db_index=True)
    localizacao = models.CharField(max_length=200)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ATIVA,
        db_index=True,
    )

    tipo = models.CharField(
        max_length=30,
        choices=TipoPlataforma.choices,
        db_index=True,
    )

    data_comissionamento = models.DateTimeField()
    data_inspecao = models.DateTimeField()

    supervisor = models.CharField(max_length=100)
    responsavel_tecnico = models.CharField(max_length=100)
    operador_principal = models.CharField(max_length=100)
    equipe_manutencao = models.CharField(max_length=100)

    observacoes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Plataforma"
        verbose_name_plural = "Plataformas"
        ordering = ["nome"]
        indexes = [
            models.Index(fields=["status", "tipo"]),
        ]

    def __str__(self) -> str:
        return self.nome


class Funcionario(models.Model):
    class Turno(models.TextChoices):
        MATUTINO = "matutino", "Matutino"
        VESPERTINO = "vespertino", "Vespertino"
        NOTURNO = "noturno", "Noturno"
        DIURNO = "diurno", "Diurno"

    class Permissao(models.TextChoices):
        OPERADOR = "operador", "Operador"
        GERENTE = "gerente", "Gerente"
        ADMINISTRADOR = "administrador", "Administrador"

    id = models.AutoField(primary_key=True)

    nome = models.CharField(max_length=100, db_index=True)
    cargo = models.CharField(max_length=100)

    permissao = models.CharField(
        max_length=20,
        choices=Permissao.choices,
        db_index=True,
    )

    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, unique=True)
    cpf = models.CharField(max_length=15, unique=True)

    turno = models.CharField(
        max_length=20,
        choices=Turno.choices,
        db_index=True,
    )

    supervisor = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)

    observacoes = models.TextField(blank=True, null=True)

    plataforma = models.ForeignKey(
        Plataforma,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="funcionarios",
        help_text="Plataforma onde o funcionário está alocado (se aplicável).",
    )

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"
        ordering = ["nome"]
        indexes = [
            models.Index(fields=["cpf"]),
            models.Index(fields=["setor"]),
        ]

    def __str__(self) -> str:
        return f"{self.nome} ({self.cargo})"


class OcorrenciaQueima(models.Model):
    class StatusComunicacao(models.TextChoices):
        PENDENTE = "pendente", "Pendente"
        ENVIADA = "enviada", "Enviada"
        FALHA = "falha", "Falha"

    id = models.AutoField(primary_key=True)

    plataforma = models.ForeignKey(
        Plataforma,
        on_delete=models.CASCADE,
        related_name="ocorrencias_queima",
    )

    funcionario = models.ForeignKey(
        Funcionario,
        on_delete=models.CASCADE,
        related_name="ocorrencias_queima",
    )

    responsavel = models.CharField(max_length=100)
    data_hora = models.DateTimeField(db_index=True)

    vazao = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Vazão registrada na ocorrência.",
    )

    gas = models.CharField(max_length=100)
    classificacao_queima = models.CharField(max_length=50, db_index=True)

    status_comunicacao = models.CharField(
        max_length=20,
        choices=StatusComunicacao.choices,
        default=StatusComunicacao.PENDENTE,
        db_index=True,
    )

    class Meta:
        verbose_name = "Ocorrência de Queima"
        verbose_name_plural = "Ocorrências de Queima"
        ordering = ["-data_hora"]
        indexes = [
            models.Index(fields=["plataforma", "data_hora"]),
        ]

    def __str__(self) -> str:
        return f"Ocorrência {self.id} - {self.classificacao_queima}"


class Equipamento(models.Model):
    class StatusOperacional(models.TextChoices):
        ATIVO = "ativo", "Ativo"
        INATIVO = "inativo", "Inativo"
        MANUTENCAO = "manutencao", "Em Manutenção"

    id = models.AutoField(primary_key=True)

    nome = models.CharField(max_length=100, db_index=True)

    status_operacional = models.CharField(
        max_length=20,
        choices=StatusOperacional.choices,
        default=StatusOperacional.ATIVO,
        db_index=True,
    )

    fabricante = models.CharField(max_length=100, blank=True, null=True)
    codigo = models.CharField(max_length=50, blank=True, null=True, db_index=True)
    numero_patrimonio = models.CharField(max_length=50, blank=True, null=True)

    observacoes = models.TextField(blank=True, null=True)

    plataforma = models.ForeignKey(
        Plataforma,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="equipamentos",
        help_text="Plataforma onde o equipamento está instalado (se aplicável).",
        db_column="ID_Plataforma",  # mantém compatibilidade com seu banco atual
    )

    class Meta:
        verbose_name = "Equipamento"
        verbose_name_plural = "Equipamentos"
        ordering = ["nome"]
        indexes = [
            models.Index(fields=["status_operacional"]),
            models.Index(fields=["codigo"]),
        ]

    def __str__(self) -> str:
        return self.nome
