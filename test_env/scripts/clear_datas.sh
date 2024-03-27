#!/bin/bash

#!/bin/bash

# PostgreSQL接続情報
DB_USER="your_username"
DB_NAME="your_database_name"

# テーブルの一覧を取得
table_list=$(docker compose exec postgresql psql -A -x -c "SELECT tablename FROM pg_tables WHERE schemaname='public';")
echo $table_list
# テーブルを削除
for table in $table_list; do
  #psql -U $DB_USER -d $DB_NAME -c "DROP TABLE IF EXISTS $table CASCADE;"
  #echo "Table $table deleted."
  echo $table
done