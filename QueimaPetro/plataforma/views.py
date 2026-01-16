# views.py
from __future__ import annotations

import base64
import io
import unicodedata
from datetime import timedelta

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from DadosQueima.models import MaterialQueimado
from database.models import Plataforma
from .forms import PlataformaForm


# Ativa/desativa modo de teste (período curto)
MODO_TESTE = False

# ==========================
# Função para pegar dados
# ==========================
def pegar_pontos(qs, n_pontos=5):
    """
    Retorna n_pontos igualmente distribuídos do início ao fim do queryset
    """
    total = qs.count()

    if total == 0:
        return []

    if total <= n_pontos:
        return list(qs)

    indices = [
        round(i * (total - 1) / (n_pontos - 1))
        for i in range(n_pontos)
    ]

    return [qs[i] for i in indices]


# ==========================
# Helpers de gráficos
# ==========================

def _salvar_grafico_em_base64() -> str:
    """
    Salva o gráfico atual do matplotlib em PNG (base64) para uso no template.
    """
    buffer = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buffer, format="png")
    buffer.seek(0)

    imagem_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
    plt.close()
    return imagem_base64


def gerar_grafico_linha(dados) -> str:
    # garante ordem por id
    dados = dados.order_by("id")

    pontos = pegar_pontos(dados)

    plt.figure(figsize=(5, 5))

    horas = []
    volumes = []

    for d in pontos:
        if d.data_queima is None:
            continue

        try:
            vol = float(d.volume_gas or 0)
        except (TypeError, ValueError):
            vol = 0.0

        horas.append(d.data_queima)
        volumes.append(vol)

    if not horas:
        plt.text(0.5, 0.5, "Sem dados para plotar", ha="center", va="center")
        plt.axis("off")
        return _salvar_grafico_em_base64()

    plt.plot(horas, volumes, marker="o")
    plt.fill_between(horas, volumes, alpha=0.1)

    ax = plt.gca()
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m %H:%M"))
    plt.gcf().autofmt_xdate()

    plt.xlabel("Data/Hora")
    plt.ylabel("Volume Total (m³)")
    plt.grid(True)

    return _salvar_grafico_em_base64()



def gerar_grafico_pizza(dados) -> str:
    tipos = {}

    for d in dados:
        tipo = getattr(d, "tipo_queima", None) or "Não informado"
        vol = getattr(d, "volume_gas", None)

        try:
            vol = float(vol) if vol is not None else 0.0
        except (TypeError, ValueError):
            vol = 0.0

        tipos[tipo] = tipos.get(tipo, 0.0) + vol

    valores = list(tipos.values())
    total = sum(valores)

    plt.figure(figsize=(4, 4))

    if total <= 0:
        plt.text(0.5, 0.5, "Sem dados para pizza", ha="center", va="center", fontsize=12)
        plt.axis("off")
        plt.title("Tipo de Queima")
        return _salvar_grafico_em_base64()

    plt.pie(valores, labels=list(tipos.keys()), autopct="%1.1f%%")

    return _salvar_grafico_em_base64()



def normalizar_nome_gas(s: str) -> str:
    if not s:
        return ""
    s = s.strip()  # tira espaços nas pontas
    # remove acentos
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    # padroniza espaços
    s = " ".join(s.split())
    return s


def gerar_grafico_barras(dados) -> str:
    gases = {}
    for d in dados:
        nome = normalizar_nome_gas(d.nome_gas)
        vol = d.volume_gas or 0
        gases[nome] = gases.get(nome, 0) + vol

    plt.figure(figsize=(5, 3))
    plt.barh(list(gases.keys()), list(gases.values()))
    plt.xlabel("Volume (m³)")

    return _salvar_grafico_em_base64()




# ==========================
# Dashboard
# ==========================

def visualizacao_grafico(request):
    agora = timezone.now()

    dados = MaterialQueimado.objects.all()

    grafico_linha = gerar_grafico_linha(dados)
    grafico_pizza = gerar_grafico_pizza(dados)
    grafico_barras = gerar_grafico_barras(dados)

    eficiencias = []
    for d in dados:
        e = getattr(d, "eficiencia", None)
        try:
            e = float(e) if e is not None else None
        except (TypeError, ValueError):
            e = None
        if e is not None:
            eficiencias.append(e)

    eficiencia_media = round(sum(eficiencias) / len(eficiencias), 2) if eficiencias else 0

    contexto = {
        "grafico_linha": grafico_linha,
        "grafico_pizza": grafico_pizza,
        "grafico_barras": grafico_barras,
        "eficiencia_media": eficiencia_media,
        "ultima_atualizacao": agora,
        "titulo": "Plataforma (todos os dados)",
    }
    return render(request, "grafico/plataforma.html", contexto)



# ==========================
# CRUD - Plataforma
# ==========================

def cadastrar(request):
    if request.method == "POST":
        form = PlataformaForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Plataforma cadastrada com sucesso!")
            return redirect("plataforma:visualizar")

        messages.error(request, "Corrija os erros no formulário.")
    else:
        form = PlataformaForm()

    return render(request, "Cadastro/index2.html", {"form": form})


def visualizar_plataforma(request):

    plataformas = Plataforma.objects.all().order_by("nome")
    return render(request, "Cadastro/cadastro.html", {"plataformas": plataformas})


def visualizar_plataformaid(request, id: int):
    plataforma = get_object_or_404(Plataforma, id=id)
    return render(request, "Visualizacao_PlataformaID/index.html", {"plataforma": plataforma})


def editar_plataforma(request, id: int):
    plataforma = get_object_or_404(Plataforma, id=id)

    if request.method == "POST":
        form = PlataformaForm(request.POST, instance=plataforma)

        if form.is_valid():
            form.save()
            messages.success(request, "Plataforma atualizada com sucesso!")
            return redirect("plataforma:visualizacaoid", id=plataforma.id)

        messages.error(request, "Corrija os erros no formulário.")
    else:
        form = PlataformaForm(instance=plataforma)

    return render(
        request,
        "Visualizacao_PlataformaID/index_editar.html",
        {"form": form, "plataforma": plataforma},
    )
