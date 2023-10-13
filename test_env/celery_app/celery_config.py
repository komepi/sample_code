# celeryconfig.py
from os import environ
# celeryを動かすための設定ファイル。
broker_url = environ['BROKER_URL']
result_backend = environ['RESULT_BACKEND']



## CELERYD_CONCURRENCY=1なので、１こずつキューを捌いていく
## ここはCPU数に合わせていくのがよい
#CELERYD_CONCURRENCY = 1
#CELERY_TASK_SERIALIZER = 'json'
#CELERY_RESULT_SERIALIZER = 'json'
#CELERY_ACCEPT_CONTENT = ['json']
#CELERYD_LOG_FILE = "./celeryd.log"
#
## CELERYD_LOG_LEVELをINFOにしておくと、
## タスクの標準出力もログ(celeryd.log)に書かれる
#CELERYD_LOG_LEVEL = "INFO"
#
## ワーカーはtasks.pyを読み込み、
## 非同期処理させる関数を
## 含むスクリプト全てを指定
#CELERY_IMPORTS = ("tasks", )