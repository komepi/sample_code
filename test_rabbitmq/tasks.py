from celery import Celery, shared_task
from time import sleep

app = Celery('tasks', backend='amqp', broker='amqp://guest:guest@rabbitmq:5672')

@shared_task(acks_late=True)
def add(x, y):
    sleep(30)
    return x + y