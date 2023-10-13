
import sys,os

sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
from src.celery.tasks import add


result = add.apply_async(args=(1, 2))
print(result)
print(type(result))
print(dir(result))
print(result.result) # タスクの戻り値
print(result.task_id) # タスクID
