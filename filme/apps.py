from django.apps import AppConfig


class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'

    def ready(self):
        from .models import Usuario
        import os

        email = os.getenv('E-MAIL_ADMIN')
        senha = os.getenv('SENHA_ADMIN')
        
        # Verifica se já existe um usuário com username='admin'
        if not Usuario.objects.filter(username='admin').exists():
            Usuario.objects.create_superuser(
                username='admin',
                email=email,
                password=senha,
                is_active=True,
                is_staff=True
            )