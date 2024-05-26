from django.apps import AppConfig


class ManUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'man_user'

    def ready(self) -> None:
        from . import signals
