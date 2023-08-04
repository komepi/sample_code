# ベースイメージの指定
FROM node:latest

# コンテナ内の作業ディレクトリの指定
WORKDIR /code

# ホストのpackage.jsonをコンテナの作業ディレクトリにコピー
COPY package.json .

# 必要なパッケージのインストール
RUN npm install

# ホストのソースコードをコンテナの作業ディレクトリにコピー
COPY . .

# コンテナを起動するコマンド
CMD ["node", "app.js"]
