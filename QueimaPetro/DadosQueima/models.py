from django.db import models
from database.models import Plataforma
import random


def plataforma_aleatoria():
    plataformas = Plataforma.objects.all()
    if plataformas.exists():
        return random.choice(plataformas)
    return None


class MaterialQueimado(models.Model):
    id = models.AutoField(primary_key=True)
    massa_kg = models.FloatField(verbose_name="Massa (kg)")
    temperatura_c = models.FloatField(verbose_name="Temperatura de Queima (°C)")
    duracao_s = models.FloatField(verbose_name="Duração (segundos)")
    data_queima = models.DateTimeField(auto_now_add=True)
    tipo_queima = models.CharField(max_length=50, default="Rotineira")
    volume_gas = models.FloatField()
    eficiencia = models.FloatField()
    nome_gas = models.CharField(max_length=100, default="Gás A")
    plataforma = models.CharField(max_length=100, default=plataforma_aleatoria)

    def __str__(self):
        return f"Queima #{self.id} - {self.temperatura_c}°C / {self.massa_kg}kg"
