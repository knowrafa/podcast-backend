from django.apps import AppConfig

default_app_config = 'management.celery.CeleryConfig'


class CeleryConfig(AppConfig):
    name = 'management.celery'
