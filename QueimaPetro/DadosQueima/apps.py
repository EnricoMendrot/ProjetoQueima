from django.apps import AppConfig


class DadosqueimaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'DadosQueima'
    
    def ready(self):
        # Importa e inicia o gerador automaticamente
        from .tasks import iniciar_gerador
        iniciar_gerador(intervalo_segundos=1000000)