from django.shortcuts import render
from datetime import timedelta
from django.utils import timezone
from .models import MaterialQueimado
from django.views.decorators.csrf import csrf_exempt

# Usado para ativar/desativar o teste
modo_teste = False

# =========== Gera dados Diarios =========== #
def dados_diarios():
    dia = timezone.now().date()

    if modo_teste:
        dia_teste = dia - timedelta(minutes=2) # Define um dia com 2 min de duração
        return MaterialQueimado.objects.filter(data_queima__date=dia_teste)
    else:
        return MaterialQueimado.objects.filter(data_queima__date=dia)

# =========== Gera dados Semanais =========== #
def dados_semanais():
    semana = timezone.now() - timedelta(days=7) 
    if modo_teste:
        semana_teste = semana - timedelta(minutes=3) # Define uma semana com 3 min de duração
        return MaterialQueimado.objects.filter(data_queima__gte=semana_teste)
    else:
        return MaterialQueimado.objects.filter(data_queima__gte=semana)
    
# =========== Gera dados Mensais =========== #
def dados_mensais():
    mes = timezone.now().replace(day=1)
    if modo_teste:
        mes_teste = mes - timedelta(minutes=5) # Define um mês com 5 minutos
        return MaterialQueimado.objects.filter(data_queima__gte=mes_teste)
    else:
        return MaterialQueimado.objects.filter(data_queima__gte=mes)

# ====== Gera dados Anuais ======= #
def dados_anuais():
    ano = timezone.now()

    if modo_teste:
        ano_teste = ano - timedelta(minutes=6) # Define um ano com duração de 6 minutos
        return MaterialQueimado.objects.filter(data_queima__gte=ano_teste)
    else:
        return MaterialQueimado.objects.filter(data_queima__year=ano.year)

# ====== Manipulação dos Dados para criação de gráficos ======= #
def plataforma_dashboard(request):
    agora = timezone.now()

    # --- Define o período (diário ou de teste) ---
    if modo_teste:
        inicio_periodo = agora - timedelta(minutes=5)
    else:
        inicio_periodo = agora.replace(hour=0, minute=0, second=0)

    # --- Busca os dados no banco ---
    dados = MaterialQueimado.objects.all()

    # --- Gera estatísticas básicas ---
    total_vq = sum(d.volume_gas for d in dados)
    eficiencia_media = round(sum(d.eficiencia for d in dados) / len(dados), 2) if dados else 0

    # --- Gera listas para o gráfico de linha (horas x volume total) ---
    horas = [d.data_queima.strftime("%H:%M") for d in dados]
    volumes = [d.volume_gas for d in dados]

    # --- Gera dados para o gráfico de pizza (tipo de queima) ---
    tipos: dict[str, float] = {"Rotineira": 0.0, "Emergencial": 0.0, "Programada": 0.0}
    for d in dados:
        tipos[d.tipo_queima] = tipos.get(d.tipo_queima, 0.0) + d.volume_gas

    # --- Dados para gráfico de barras (VQ por gás) ---
    gases = {}
    for d in dados:
        gases[d.nome_gas] = gases.get(d.nome_gas, 0) + d.volume_gas

    contexto = {
        "titulo": "Plataforma 1",
        "horas": horas,
        "volumes": volumes,
        "tipos": tipos,
        "gases": gases,
        "total_vq": total_vq
    } 