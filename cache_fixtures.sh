#!/usr/bin/env bash

rm -f db.sqlite3
curl -XDELETE http://127.0.0.1:9200/dbsqlite3_content_tag_0001
curl -XDELETE http://127.0.0.1:9200/dbsqlite3_content_content_0001
python manage.py migrate --noinput
python manage.py synces 0001
python manage.py es_swap_aliases 0001
python manage.py create_test_data

mv db.sqlite3 cache.sqlite3
curl -XDELETE http://127.0.0.1:9200/dbsqlite3_content_tag_0001
curl -XDELETE http://127.0.0.1:9200/dbsqlite3_content_content_0001