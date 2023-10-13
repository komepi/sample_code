import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
from celery_app.app import app
from celery import shared_task

@shared_task
def add(x,y):
    ret = x + y
    print("result:{}".format(ret))
    return ret