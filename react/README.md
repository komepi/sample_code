1. ビルド
    ```cmd
    docker compose build
    ```
2. プロジェクト作成
    ```cmd
    docker compose run --rm app sh -c 'npx create-react-app react-app --template typescript'
    ```
    react-appがプロジェクト名で、ディレクトリ名でもある
    それぞれ以下のような命令
    |オプション/コマンド|機能|
    |:--|:--|
    |--template typescript|typescriptをインストール。ないとjsになる|
    |-rm|コンテナを起動後削除|
    |sh -c ~|コンテナ起動後に実行するコマンド|
    コンテナ起動->コマンドによりプロジェクト作成->コンテナ削除の順で処理が進む
    これによりappディレクトリ下にプロジェクトが作成される
3. コンテナ起動
    ```cmd
    docker compose up -d
    ```
    起動後http://localhost:3000にアクセスできる