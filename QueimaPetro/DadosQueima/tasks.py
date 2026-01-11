import random
import threading
from django.utils import timezone
from .models import MaterialQueimado

def gerar_dados_queima():
    temperatura = round(random.uniform(200, 800), 1)  # °C
    volume_gas = round(random.uniform(0, 100), 3)  # °C
    duracao = round(random.uniform(5, 120), 2)        # segundos
    massa = round(random.uniform(0.1, 2.0), 3)        # kg
    eficiencia = round(random.uniform(70, 100), 2)    # %
    eficiencia = round(random.uniform(70, 100), 2)    # %
    tipo_queima = random.choice(["Rotineira", "Emergencial", "Programada"])
    nome_gas = random.choice(["Gas A", "Gas B", "Gas C", "Gas D", "Gas E"])
    nome_empresa = random.choice(["Empresa 1", "Empresa 2", "Empresa 3", "Empresa 4", "Empresa 5", "Empresa 6"])
    data_queima = timezone.now()

    registro = MaterialQueimado.objects.create(
        temperatura_c=temperatura,
        duracao_s=duracao,
        massa_kg=massa,
        eficiencia=eficiencia,
        tipo_queima=tipo_queima,
        data_queima=data_queima,
        nome_gas = nome_gas,
        volume_gas = volume_gas
    )

    # print(f"[AUTO GERADOR] Queima criada: ID={registro.id} | {tipo_queima} | {temperatura}°C | {massa}kg | {duracao}s | {eficiencia}% | {nome_gas}| {nome_empresa}")

def iniciar_gerador(intervalo_segundos=90000):
    """Executa o gerador automaticamente a cada X segundos."""
    def agendar():
        gerar_dados_queima()
        threading.Timer(intervalo_segundos, agendar).start()
    threading.Timer(intervalo_segundos, agendar).start()