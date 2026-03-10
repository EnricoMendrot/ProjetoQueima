from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "database",
            "0015_remove_funcionario_empresa",
        ),  # <- troque para a sua última migration real
    ]

    operations = [
        # ===== Equipamento =====
        migrations.RenameField("equipamento", "Nome", "nome"),
        migrations.RenameField("equipamento", "Codigo", "codigo"),
        migrations.RenameField("equipamento", "Numero_Patrimonio", "numero_patrimonio"),
        migrations.RenameField(
            "equipamento", "Status_Operacional", "status_operacional"
        ),
        migrations.RenameField("equipamento", "Plataforma", "plataforma"),
        # ===== Funcionario =====
        migrations.RenameField("funcionario", "Nome", "nome"),
        migrations.RenameField("funcionario", "Email", "email"),
        migrations.RenameField("funcionario", "Permissao", "permissao"),
        migrations.RenameField("funcionario", "Turno", "turno"),
        migrations.RenameField("funcionario", "ID_Plataforma", "plataforma"),
        # ===== Plataforma =====
        migrations.RenameField("plataforma", "Nome", "nome"),
        migrations.RenameField("plataforma", "Status", "status"),
        migrations.RenameField("plataforma", "Tipo", "tipo"),
        migrations.RenameField("plataforma", "Observacoes", "observacoes"),
        # ===== OcorrenciaQueima =====
        migrations.RenameField("ocorrenciaqueima", "Data_Hora", "data_hora"),
        migrations.RenameField(
            "ocorrenciaqueima", "ClassificacaoQueima", "classificacao_queima"
        ),
        migrations.RenameField(
            "ocorrenciaqueima", "statuscomunicacao", "status_comunicacao"
        ),
        migrations.RenameField("ocorrenciaqueima", "ID_Funcionario", "funcionario"),
        migrations.RenameField("ocorrenciaqueima", "ID_Plataforma", "plataforma"),
        migrations.RenameField("ocorrenciaqueima", "Vazao", "vazao"),
    ]
