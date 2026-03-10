import random
import threading
from django.utils import timezone
from .models import MaterialQueimado
from database.models import Plataforma


def pegar_plataforma():
    plataformas = Plataforma.objects.all()
    if plataformas.exists():
        return random.choice(plataformas)
    return None


def gerar_dados_queima():
    plataforma_escolhida = pegar_plataforma()

    # Se não houver plataforma cadastrada, não cria registro
    if not plataforma_escolhida:
        print("Nenhuma plataforma cadastrada.")
        return

    temperatura = round(random.uniform(200, 800), 1)
    volume_gas = round(random.uniform(0, 100), 3)
    duracao = round(random.uniform(5, 120), 2)
    massa = round(random.uniform(0.1, 2.0), 3)
    eficiencia = round(random.uniform(70, 100), 2)

    tipo_queima = random.choice(["Rotineira", "Emergencial", "Programada"])
    nome_gas = random.choice(["Gas A", "Gas B", "Gas C", "Gas D", "Gas E"])
    data_queima = timezone.now()

    registro = MaterialQueimado.objects.create(
        temperatura_c=temperatura,
        duracao_s=duracao,
        massa_kg=massa,
        eficiencia=eficiencia,
        tipo_queima=tipo_queima,
        data_queima=data_queima,
        nome_gas=nome_gas,
        volume_gas=volume_gas,
        plataforma=plataforma_escolhida,
    )

    print(
        f"[AUTO GERADOR] Queima criada: ID={registro.id} | {tipo_queima} | {temperatura}°C | {massa}kg | {duracao}s | {eficiencia}% | {nome_gas}| {plataforma_escolhida}"
    )


def iniciar_gerador(intervalo_segundos=300):
    def agendar():
        gerar_dados_queima()
        threading.Timer(intervalo_segundos, agendar).start()

    threading.Timer(intervalo_segundos, agendar).start()
