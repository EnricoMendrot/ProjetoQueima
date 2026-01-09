# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.utils import timezone
from .forms import PlataformaForm
from django.contrib import messages
from DadosQueima.models import MaterialQueimado

from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from database.models import Plataforma
import io
import base64
from datetime import timedelta
import matplotlib.dates as mdates


# # Usado para ativar/desativar o teste
modo_teste = False
# ==================================== Função de Mostrar os gráficos ==================================== #     

# =============== LINHAS =============== #
def gerar_grafico_linha(dados):
    plt.figure(figsize=(5,5))

    # PEGUE A DATA REAL
    horas = [d.data_queima for d in dados]
    volumes = [d.volume_gas for d in dados]

    plt.plot(horas, volumes, marker="o", color="red")
    plt.fill_between(horas, volumes, color="red", alpha=0.1)

    # =======Controlar o tempo do gráfico de linhas======== #
    ax = plt.gca()
    ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=10))   # a cada 10 min
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))     # formato do tick

    plt.gcf().autofmt_xdate()

    plt.title("VQ do Gás Total Queimado na Plataforma")
    plt.xlabel("Horário")
    plt.ylabel("Volume Total (m³)")
    plt.grid(True)

    return salvar_grafico_em_base64()

# =============== PIZZA =============== #
def gerar_grafico_pizza(dados):
    tipos = {"Rotineira": 0, "Emergencial": 0, "Programada": 0}
    for d in dados:
        tipos[d.tipo_queima] = tipos.get(d.tipo_queima, 0) + d.volume_gas

    plt.figure(figsize=(4,4))
    labels = list(tipos.keys())
    valores = list(tipos.values())
    plt.pie(valores, labels=labels, autopct='%1.1f%%')
    plt.title("Tipo de Queima (Diário)")
    return salvar_grafico_em_base64()

# =============== BARRAS =============== #
def gerar_grafico_barras(dados):
    gases = {}
    for d in dados:
        gases[d.nome_gas] = gases.get(d.nome_gas, 0) + d.volume_gas

    plt.figure(figsize=(5,3))
    chaves = list(gases.keys())
    valores = list(gases.values())
    plt.barh(chaves, valores, color="green")
    plt.title("VQ por Gás")
    plt.xlabel("Volume (m³)")
    return salvar_grafico_em_base64()

# ====================== SALVA OS GRAFICOS =================  #
def salvar_grafico_em_base64():
    buffer = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    imagem_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    plt.close()

    print("[DEBUG] Gráfico gerado com sucesso!")
    return imagem_base64

# =============== DASHBOARD =============== #
def visualizacao_grafico(request):
    agora = timezone.now()
    if modo_teste:
        inicio_periodo = agora - timedelta(minutes=5)
    else:
        inicio_periodo = agora.replace(hour=0, minute=0, second=0)

    dados = MaterialQueimado.objects.filter(data_queima__gte=inicio_periodo)

    # Gera os gráficos
    grafico_linha = gerar_grafico_linha(dados)
    grafico_pizza = gerar_grafico_pizza(dados)
    grafico_barras = gerar_grafico_barras(dados)

    # Calcula eficiência média
    eficiencia_media = round(sum(d.eficiencia for d in dados)/len(dados), 2) if dados else 0

    contexto = {
        "grafico_linha": grafico_linha,
        "grafico_pizza": grafico_pizza,
        "grafico_barras": grafico_barras,
        "eficiencia_media": eficiencia_media,
        "data_atualizacao": agora.strftime("%d/%m/%Y %H:%M"),
        "titulo": "Plataforma 1"
    }

    return render(request, 'grafico/plataforma.html', contexto)

#=============================================== Cadastrar ===============================================#

def cadastrar(request):
    if request.method == "POST":
        form = PlataformaForm(request.POST)

        print("POST RECEBIDO:", request.POST)

        if form.is_valid():
            print("FORM OK")
            form.save()
            return redirect("plataforma:visualizar")
        else:
            print("FORM INVÁLIDO")
            print(form.errors)

    else:
        form = PlataformaForm()

    return render(request, "Cadastro/index2.html", {"form": form})

#=========================================== Visualizacao =============================================#

def visualizar_plataforma(request):
    return render(request, "Cadastro/cadastro.html")

#========================================= Visualizar por ID ==========================================#

def visualizar_plataformaid(request, ID_Plataforma):
    plataforma = get_object_or_404(Plataforma, ID_Plataforma=ID_Plataforma)
    contexto = {
        "plataforma": plataforma

    }
    return render(request, 'Visualizacao_PlataformaID/index.html', contexto)

#=================Editar Visualização================#

def editar_plataforma(request, ID_Plataforma):
    plataforma = get_object_or_404(Plataforma, ID_Plataforma=ID_Plataforma)
    
    if request.method == "POST":
        form = PlataformaForm(request.POST, instance=plataforma)
        
        if form.is_valid():  # Com parênteses!
            form.save()
            messages.success(request, 'Plataforma atualizada com sucesso!')
            return redirect("plataforma:visualizacaoid", ID_Plataforma=plataforma.ID_Plataforma)
        else:
            # Temporário para debug: mostra erros no terminal
            print("=== FORMULÁRIO INVÁLIDO ===")
            print(form.errors)
            print("Dados POST recebidos:", request.POST)
            
            messages.error(request, 'Corrija os erros no formulário.')
    
    else:
        form = PlataformaForm(instance=plataforma)
    
    contexto = {
        'form': form,
        'plataforma': plataforma
    }
    
    return render(request, 'Visualizacao_PlataformaID/index_editar.html', contexto)