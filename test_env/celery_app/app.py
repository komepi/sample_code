from os import environ
from celery import Celery

environ.setdefault('CELERY_CONFIG_MODULE', 'celery_app.celery_config')

app = Celery()
app.config_from_envvar('CELERY_CONFIG_MODULE')
app.autodiscover_tasks()
app.conf.imports = ['src.celery.tasks']
