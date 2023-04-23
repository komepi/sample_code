# main.py
from celery.task.control import revoke

import tasks
print('<first task>')
# ここでタスク起動　(runタスク)
worker = tasks.run.delay()
task_id = worker.id
print("関係ないタスクrevoke")
revoke("123454",terminate=True)
print(worker.state)
#worker._cache={"status":"REJECTED"}
worker._cache={"status":"RETRY"}
print(worker.state)
# 終わらぬなら終わるまで待とうホトトギス
#print("revoke")
#revoke(task_id)
#print("revoke terminate")
revoke(task_id, terminate=True)
print(worker.state)
while not worker.ready():
   pass
# 返り値をだす
print("owata")
print(worker.result)
print(worker.state)


print(worker.state)
print('<second task>')
# ここでタスク起動　(calcタスク)
worker = tasks.calc.delay(100, 200)
# 終わらぬなら終わるまで待とうホトトギス
while not worker.ready():
   pass
# 返り値をだす
print(worker.result)