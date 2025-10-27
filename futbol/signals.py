from django.db.models.signals import post_migrate
from django.contrib.auth import get_user_model
from django.dispatch import receiver
import os

@receiver(post_migrate)
def create_superuser_on_deploy(sender, **kwargs):
    """Crea un superusuario automáticamente cuando se termina migrate (Render Free compatible)."""
    if os.environ.get("RENDER_CREATE_SUPERUSER") == "true":
        User = get_user_model()
        username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "Admin12345")

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            print(f"✅ Superusuario '{username}' creado automáticamente.")
        else:
            print("ℹ️ El superusuario ya existe.")
