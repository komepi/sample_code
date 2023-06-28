# tasks.py
import os
import time
import celery
import celeryconfig
from celery import shared_task

CELERY_BROKER = os.environ.get('CELERY_BROKER')
CELERY_BACKEND = os.environ.get('CELERY_BACKEND')

app = celery.Celery(
  'tasks',
  broker=CELERY_BROKER,
  backend=CELERY_BACKEND
)
app.config_from_object(celeryconfig)

@app.task
def run():
   print("処理　はじまた")
   time.sleep(10)
   print('処理　おわた')
   return 'おわったよ'

@app.task
def calc(a, b):
   return a+b


@shared_task
def task1():
   print("start task1")
   task2.apply_async()
   time.sleep(60)

@shared_task
def task2():
   print("start task2")
   time.sleep(60)


@shared_task
def task3():
   print("start task3")
   time.sleep(60)