from django.db import models

class MaterialQueimado(models.Model):
    id = models.AutoField(primary_key=True)
    massa_kg = models.FloatField(verbose_name="Massa (kg)")
    temperatura_c = models.FloatField(verbose_name="Temperatura de Queima (°C)")
    duracao_s = models.FloatField(verbose_name="Duração (segundos)")
    data_queima = models.DateTimeField(verbose_name="Data/Hora da Queima")

    def __str__(self):
        return f"Queima #{self.id} - {self.temperatura_c}°C / {self.massa_kg}kg"
