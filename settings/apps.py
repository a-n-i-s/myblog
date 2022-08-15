from django.apps import AppConfig


class SettingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'settings'

    def ready(self) -> None:
        from .signals import create_usersetting
        return super().ready()
