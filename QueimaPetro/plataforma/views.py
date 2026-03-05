# views.py
from __future__ import annotations

import base64
import io
import unicodedata
from datetime import timedelta
from datetime import datetime

import matplotlib
matplotlib.use('Agg')
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
    total = len(qs)

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
    plt.close("all")
    return imagem_base64

def gerar_grafico_linha(dados) -> str:
    
    dados = sorted(dados, key=lambda x: x.id)

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

    plt.plot(horas, volumes, marker="o", color="#009c98")
    plt.fill_between(horas, volumes, alpha=0.1)

    ax = plt.gca()
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m %H:%M"))
    plt.gcf().autofmt_xdate()

    plt.xlabel("Data/Hora")
    plt.ylabel("Volume Total (m³)")
    plt.grid(True)

    return _salvar_grafico_em_base64()

def gerar_grafico_rosca(dados) -> str:
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
    
    plt.figure(figsize=(5, 4))

    if total <= 0:
        plt.text(0.5, 0.5, "Sem dados para rosca", ha="center", va="center", fontsize=12)
        plt.axis("off")
        return _salvar_grafico_em_base64()

    cores = ["#00d27f", "#00b892", "#009c98", "#007f8f"]
    plt.rcParams["font.family"] = "Arial"

    total = sum(valores)

    # labels com o nome + %
    labels_formatadas = [
        f"{nome} {valor/total*100:.2f}%" for nome, valor in tipos.items()
    ]

    wedges, texts = plt.pie(
        valores,
        labels=labels_formatadas,
        wedgeprops=dict(width=0.4),
        startangle=90,
        labeldistance=1.2,
        colors=cores
    )

    # Ajuste a fonte dos textos
    for text in texts:
        text.set_fontsize(11)   
    
    plt.axis("equal")  # mantém o formato circular

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
    if not gases:
        plt.text(0.5, 0.5, "Sem dados para barras", ha="center", va="center", fontsize=12)
        plt.axis("off")
        return _salvar_grafico_em_base64()

    plt.barh(list(gases.keys()), list(gases.values()), color="#009c98")
    plt.xlabel("Volume (m³)")

    return _salvar_grafico_em_base64()

# ========================== 
# Dashboard                     
# ========================== 

def visualizacao_grafico(request):
    agora = timezone.now()
    dados = MaterialQueimado.objects.all()

    nome_plataforma = request.GET.get('plataforma')
    data_selecionada = request.GET.get('data')

    # 🔹 Filtro por plataforma
    if nome_plataforma:
        dados = dados.filter(plataforma=nome_plataforma)

    # 🔹 Filtro por data
    if data_selecionada:
        try:
            data_convertida = datetime.strptime(data_selecionada, "%Y-%m-%d")

            inicio = data_convertida
            fim = data_convertida + timedelta(days=1)

            dados = dados.filter(
                data_queima__gte=inicio,
                data_queima__lt=fim
            )

        except ValueError:
            pass

    dados_lista = list(dados)

    grafico_linha = gerar_grafico_linha(dados_lista)
    grafico_rosca = gerar_grafico_rosca(dados_lista)
    grafico_barras = gerar_grafico_barras(dados_lista)

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
        "grafico_rosca": grafico_rosca,
        "grafico_barras": grafico_barras,
        "eficiencia_media": eficiencia_media,
        "ultima_atualizacao": agora,
        "titulo": nome_plataforma,
        "data_selecionada": data_selecionada,
    }

    return render(request, "ExibiçãoDetalhada/Resumo_Detalhado.html", contexto)


# ==========================
# CRUD - Plataforma
# ==========================

def home(request):
    agora = timezone.now()

    plataformas = MaterialQueimado.objects.values_list('plataforma', flat=True).distinct()
    
    plataformas_dados = []
    
    for plataforma in plataformas:
        dados = MaterialQueimado.objects.filter(plataforma=plataforma)

        volume_valor = sum([getattr(d, "volume_gas", 0) for d in dados if getattr(d, "volume_gas", 0) is not None])
        
        # Formata para o padrão brasileiro: 1.234.567,89
        volume_total = f"{volume_valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") + " m³"

        grafico_rosca = gerar_grafico_rosca(dados)

        plataformas_dados.append({
            "nome": plataforma,
            "volume_total": volume_total,
            "grafico_rosca": grafico_rosca
        })

    contexto = {
        "plataformas_dados": plataformas_dados,
        "ultima_atualizacao": agora,
    }
    
    return render(request, "ExibicaoSimples/Resumo_Diario.html", contexto)
    
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

# ========== Visualizar ========== #
def visualizar_plataforma(request):

    queryset = Plataforma.objects.all()

    # Pegar os valores dos filtros (GET)
    nome = request.GET.get('nome', '').strip()
    status = request.GET.get('status', '').strip()
    id_plt = request.GET.get('id', '').strip()
    localizacao = request.GET.get('localizacao', '').strip()

    # Aplicar filtros apenas se o campo tiver valor
    if nome:
        queryset = queryset.filter(nome__icontains=nome)

    if status:
        queryset = queryset.filter(status_operacional=status)

    if id_plt:
        try:
            id_int = int(id_plt)
            queryset = queryset.filter(id=id_int)
        except ValueError:
            pass  # ignora se não for número válido

    if localizacao:
        queryset = queryset.filter(localizacao__icontains=localizacao)

    # Ordenar (opcional, mas recomendado)
    queryset = queryset.order_by('id')

    contexto = {
        'plataforma': queryset,
    }

    return render(request, "Visualizar/plataformas_cadastradas.html", contexto)


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
