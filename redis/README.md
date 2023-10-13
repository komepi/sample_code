redis実行用環境

`docker compose build`でイメージをビルド
`docker compose up -d`でコンテナを起動する
起動すると、redisとredis-pythonが起動する
redis: redis用コンテナ
redis-python: pythonコンテナ
pythonコンテナにはredisがインストールされている。他にインストールしたいパッケージがあればrequirements.txtに追加

shellにアクセスするにはvscodeからならアクティビティバー -> Docker -> redis -> アクセスしたいコンテナで右クリック -> Attach Shell
コマンドからなら`docker compose exec redis bash`, `docker compose python bash`