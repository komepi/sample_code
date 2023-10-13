postgresql実行用環境

`docker compose build`でイメージをビルド
`docker compose up -d`でコンテナを起動する
起動すると、postgresql-dbとpostgresql-python3が起動する
postgresql-db: DB用コンテナ
postgresql-python3: pythonコンテナ
pythonコンテナにはsqlalchemyがインストールされている。他にインストールしたいパッケージがあればrequirements.txtに追加

shellにアクセスするにはvscodeからならアクティビティバー -> Docker -> postgresql -> アクセスしたいコンテナで右クリック -> Attach Shell
コマンドからなら`docker compose exec db bash`, `docker compose python3 bash`