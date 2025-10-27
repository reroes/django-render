from django.apps import AppConfig


class FutbolConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'futbol'
    
    # def ready(self):
    #     import futbol.signals  # Importa las señales al iniciar
