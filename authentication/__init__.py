from django.apps import AppConfig

default_app_config = 'authentication.AuthenticationConfig'


class AuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'
