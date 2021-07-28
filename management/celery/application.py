import os

from celery import Celery
from django.conf import settings
from kombu import Queue

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings.APPLICATION_NAME + '.settings')

celery_app = Celery(settings.APPLICATION_NAME)
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()
celery_app.conf.task_default_queue = 'default'
celery_app.conf.task_queues = (
    Queue('log', routing_key=settings.APPLICATION_NAME + '.log'),
)

celery_app.conf.task_default_exchange = settings.APPLICATION_NAME
celery_app.conf.task_default_exchange_type = 'direct'
celery_app.conf.task_default_routing_key = settings.APPLICATION_NAME + '.default'

celery_app.conf.timezone = 'UTC'
