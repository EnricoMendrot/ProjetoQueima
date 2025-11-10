import random
import threading
from datetime import datetime
from .models import MaterialQueimado  # ajuste o nome do modelo conforme o seu

def gerar_dados_queima():
    """Gera e salva um registro de queima simples no banco."""
    temperatura = round(random.uniform(200, 800), 1)   # °C
    duracao = round(random.uniform(5, 120), 2)         # segundos
    massa = round(random.uniform(0.1, 2.0), 3)         # kg
    data_queima = datetime.now()

    registro = MaterialQueimado.objects.create(
        temperatura_c=temperatura,
        duracao_s=duracao,
        massa_kg=massa,
        data_queima=data_queima
    )
    print(f"[AUTO GERADOR] Queima criada: {registro.id} ({temperatura}°C, {massa}kg, {duracao}s)")

def iniciar_gerador(intervalo_segundos=60):
    """Roda o gerador automaticamente a cada X segundos."""
    def agendar():
        gerar_dados_queima()
        threading.Timer(intervalo_segundos, agendar).start()
    threading.Timer(intervalo_segundos, agendar).start()